import win32gui, win32ui, win32con
import numpy as np
import cv2
from config import Common, MuMuGeometry
from static import config
from PyQt5.QtCore import QThread
import requests


def get_window_name():
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, title in hwnd_title.items():
        if title is not "" and "模拟器" in title:
            return title


def get_windows_info():
    windows_info = config.VIDEO_INFO_INIT
    try:
        windows_name = get_window_name()
        # 获取窗口句柄
        simulator_handle = win32gui.FindWindow(None, windows_name)
        # 将窗口放在前台，并激活该窗口（窗口不能最小化）
        if win32gui.GetForegroundWindow() != simulator_handle:
            QThread.msleep(2000)
            win32gui.ShowWindow(simulator_handle, win32con.SW_SHOWNORMAL)
            win32gui.SetForegroundWindow(simulator_handle)
        # 获取窗口的位置信息
        left, top, right, bottom = win32gui.GetWindowRect(simulator_handle)
        # 窗口长宽
        width = right - left
        height = bottom - top
        # 移动窗口
        win32gui.MoveWindow(simulator_handle,
                            MuMuGeometry.X,
                            MuMuGeometry.Y,
                            MuMuGeometry.WIDTH,
                            MuMuGeometry.HEIGHT,
                            True)
        # 开始截图
        # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
        handle_window_dc = win32gui.GetWindowDC(simulator_handle)
        # 创建设备描述表
        dc = win32ui.CreateDCFromHandle(handle_window_dc)
        # 创建内存设备描述表
        save_dc = dc.CreateCompatibleDC()
        # 创建位图对象准备保存图片
        save_bitmap = win32ui.CreateBitmap()
        # 为bitmap开辟存储空间
        save_bitmap.CreateCompatibleBitmap(dc, width, height)
        # 将截图保存到saveBitMap中
        save_dc.SelectObject(save_bitmap)
        # 保存bitmap到内存设备描述表
        save_dc.BitBlt((0, 0), (width, height), dc, (0, 0), win32con.SRCCOPY)
        signed_ints_array = save_bitmap.GetBitmapBits(True)
        im_opencv = np.frombuffer(signed_ints_array, dtype='uint8')
        im_opencv.shape = (height, width, 4)
        im_opencv = cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
        # 释放内存
        win32gui.DeleteObject(save_bitmap.GetHandle())
        save_dc.DeleteDC()
        dc.DeleteDC()
        win32gui.ReleaseDC(simulator_handle, handle_window_dc)
        # 组装数据
        windows_info = {
            Common.KEY_VIDEO_LEFT: left,
            Common.KEY_VIDEO_TOP: top,
            Common.KEY_VIDEO_RIGHT: right,
            Common.KEY_VIDEO_BOTTOM: bottom,
            Common.KEY_VIDEO_WIDTH: width,
            Common.KEY_VIDEO_HEIGHT: height,
            Common.KEY_SCREEN_CAPTURE: im_opencv,
            Common.KEY_SIMULATOR_HANDLE: simulator_handle
        }
    except:
        pass
    return windows_info


def reg_template(screen_capture, template):
    """
    以左上角为原点，在原图中找出模板，如果找到则用红框圈出，弱没有找到则find_flag返回False
    :param screen_capture: 屏幕图像image
    :param template: 模板图像image
    :return: 原图+框出模板，是否找到模板，(left,top),(right,bottom)
    """
    left_top = [0, 0]
    right_bottom = [0, 0]
    img_gray = cv2.cvtColor(screen_capture, cv2.COLOR_RGB2GRAY)
    width, height = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = config.TEMPLATE_SIMILARITY_THRESHOLD
    candidate_loc = np.where(res >= threshold)
    find_flag = False
    # 画方框，[0,0,255] 颜色，2 线宽
    for left_top in zip(*candidate_loc[::-1]):
        left_top = list(left_top)
        right_bottom = [left_top[0] + width, left_top[1] + height]
        find_flag = True
        break
    return find_flag, left_top, right_bottom


def send_message(title, message):
    response = requests.get(
        "http://wx.xtuis.cn/{0}.send?text={1}&desp={2}".format(config.NOTIFY_TOKEN, title, message))
