import random

import cv2
import numpy as np
import pyautogui
from PyQt5.QtCore import QThread, pyqtSignal

from config import Common
from res.url import ResUrl, ImageKey
from static import config
from util import get_windows_info, reg_template


class Engine:
    def __init__(self):
        self.video_info = config.VIDEO_INFO_INIT
        self.reg_info = config.REG_INFO_INIT
        self.capture_thread = CaptureThread()  # 实例化线程对象
        self.capture_thread.video_info_signal.connect(self.set_video_info)
        self.reg_thread = RegThread()
        self.reg_thread.reg_info_signal.connect(self.set_reg_info)

    def start_engine(self):
        self.capture_thread.start()
        self.reg_thread.start()

    def set_video_info(self, video_info):
        self.video_info = video_info

    def set_reg_info(self, reg_info):
        self.reg_info = reg_info


class CaptureThread(QThread):  # 线程类
    """
    该线程用于捕获图像
    """
    video_info_signal = pyqtSignal(dict)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(CaptureThread, self).__init__()
        self.video_info = config.VIDEO_INFO_INIT

    def run(self):  # 线程执行函数
        while True:
            self.video_info = get_windows_info()
            self.video_info_signal.emit(self.video_info)  # 释放自定义的信号
            # 通过自定义信号把video_info传递给槽函数
            self.msleep(config.CAPTURE_INTERVAL_TIME)  # 本线程睡眠n毫秒


class RegThread(QThread):
    """
    该线程只用来在捕获的图像中，竟可能地捕获模板，用红框圈出
    """
    reg_info_signal = pyqtSignal(dict)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(RegThread, self).__init__()
        self.reg_info = config.REG_INFO_INIT

    def run(self):  # 线程执行函数
        while True:
            video_info = engine.video_info  # 释放自定义的信号
            screen_capture = video_info[Common.KEY_SCREEN_CAPTURE]
            if screen_capture is not None:
                screen_capture = screen_capture.copy()
                # TODO 扩展功能，目前只写刷御魂
                find_result = {}
                for key in ResUrl.MIKUN_ALL:
                    file_path = ResUrl.MIKUN_ALL[key]
                    template = cv2.imread(file_path, 0)
                    screen_capture, find_flag, left_top, right_bottom = reg_template(screen_capture, template)
                    if find_flag:
                        find_result[key] = {"left_top": left_top,
                                            "right_bottom": right_bottom}
                        # 模拟点击
                        # if key == ImageKey.KEY_CHALLENGE:
                        #     left = left_top[0]
                        #     top = left_top[1]
                        #     right = right_bottom[0]
                        #     bottom = right_bottom[1]
                        #     # 计算中间点
                        #     mid_x = (left + right) / 2
                        #     mid_y = (top + bottom) / 2
                        #     # 随机位移
                        #     mid_x += random.randint(-config.RANDOM_SHIFT_PIXEL, config.RANDOM_SHIFT_PIXEL)
                        #     mid_y += random.randint(--config.RANDOM_SHIFT_PIXEL, config.RANDOM_SHIFT_PIXEL)
                        #     # 随机时间位移
                        #     pyautogui.moveTo(mid_x, mid_y, duration=random.randint(1, config.RANDOM_SHIFT_TIME))
                        #     pyautogui.click()
                self.reg_info[Common.KEY_REG_IMAGE] = screen_capture
                self.reg_info[Common.KEY_REG_FIND] = find_result
            self.msleep(config.REG_INTERVAL_TIME)  # 本线程睡眠n毫秒


engine = Engine()
