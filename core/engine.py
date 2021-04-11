from util import get_windows_info
from PyQt5.QtCore import QThread, pyqtSignal
from static import config


class Engine:
    def __init__(self):
        self.video_info = config.VIDEO_INFO_INIT
        self.capture_thread = CaptureThread()  # 实例化线程对象
        self.capture_thread.video_info_signal.connect(self.set_video_info)

    def start_capture(self):
        self.capture_thread.start()

    def set_video_info(self, video_info):
        self.video_info = video_info


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


engine = Engine()
