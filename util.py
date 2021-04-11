import win32gui, win32ui, win32con
import numpy as np
import cv2
from config import Common, MuMuGeometry
from static import config


def get_window_name():
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, title in hwnd_title.items():
        if title is not "" and "阴阳师" in title:
            return title


def get_windows_info():
    windows_info = config.VIDEO_INFO_INIT
    try:
        windows_name = get_window_name()
        # 获取窗口句柄
        handle_window = win32gui.FindWindow(None, windows_name)
        # 将窗口放在前台，并激活该窗口（窗口不能最小化）
        win32gui.ShowWindow(handle_window, win32con.SW_SHOWNORMAL)
        win32gui.SetForegroundWindow(handle_window)
        # 获取窗口的位置信息
        left, top, right, bottom = win32gui.GetWindowRect(handle_window)
        # 窗口长宽
        width = right - left
        height = bottom - top
        # 移动窗口
        win32gui.MoveWindow(handle_window,
                            MuMuGeometry.X,
                            MuMuGeometry.Y,
                            MuMuGeometry.WIDTH,
                            MuMuGeometry.HEIGHT,
                            True)
        # 开始截图
        # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
        handle_window_dc = win32gui.GetWindowDC(handle_window)
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
        # 组装数据
        windows_info = {
            Common.KEY_VIDEO_LEFT: left,
            Common.KEY_VIDEO_TOP: top,
            Common.KEY_VIDEO_RIGHT: right,
            Common.KEY_VIDEO_BOTTOM: bottom,
            Common.KEY_VIDEO_WIDTH: width,
            Common.KEY_VIDEO_HEIGHT: height,
            Common.KEY_SCREEN_CAPTURE: im_opencv
        }
    except:
        pass
    return windows_info
