from PyQt5.QtCore import QThread, pyqtSignal

from static import config
from config import Common
from util import get_windows_info
import cv2
from res.url import ResUrl
import numpy as np


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
    video_info_signal = pyqtSignal(dict)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(CaptureThread, self).__init__()
        self.video_info = config.VIDEO_INFO_INIT

    def run(self):  # 线程执行函数
        while True:
            self.video_info = get_windows_info()
            self.video_info_signal.emit(self.video_info)  # 释放自定义的信号
            # 通过自定义信号把video_info传递给槽函数
            self.msleep(100)  # 本线程睡眠n毫秒


class RegThread(QThread):
    reg_info_signal = pyqtSignal(dict)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(RegThread, self).__init__()
        self.reg_info = config.REG_INFO_INIT

    def do_reg(self, screen_capture, template):
        left_top = (0, 0)
        right_bottom = (0, 0)
        img_gray = cv2.cvtColor(screen_capture, cv2.COLOR_RGB2GRAY)
        width, height = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = config.SIMILARITY_THRESHOLD
        candidate_loc = np.where(res >= threshold)
        find_flag = False
        # 画方框，[0,0,255] 颜色，2 线宽
        for left_top in zip(*candidate_loc[::-1]):
            right_bottom = (left_top[0] + width, left_top[1] + height)
            cv2.rectangle(screen_capture, left_top, right_bottom, (255, 0, 0), 2)
            find_flag = True
        return screen_capture, find_flag, left_top, right_bottom

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
                    screen_capture, find_flag, left_top, right_bottom = self.do_reg(screen_capture, template)
                    if find_flag:
                        find_result[key] = {"left_top": left_top,
                                            "right_bottom": right_bottom}
                    self.reg_info[Common.KEY_REG_IMAGE] = screen_capture
                    self.reg_info[Common.KEY_REG_FIND] = find_result
            self.msleep(100)  # 本线程睡眠n毫秒


engine = Engine()
