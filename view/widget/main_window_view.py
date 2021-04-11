from PyQt5.QtWidgets import QMainWindow

from config import Common, MainWindowGeometry
from core.engine import engine
from PyQt5.QtCore import QThread, pyqtSignal
from view.design.main_window import Ui_MainWindow
from static import config
import numpy as np
from PyQt5.QtGui import QImage, QPixmap


class MainWindowView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.init_widget()
        self.video_info = config.VIDEO_INFO_INIT
        self.video_thread = VideoThread()  # 实例化线程对象
        self.video_thread.screen_capture_signal.connect(self.update_video)
        self.video_thread.start()
        engine.start_capture()

    def init_widget(self):
        self.setGeometry(MainWindowGeometry.X,
                         MainWindowGeometry.Y,
                         MainWindowGeometry.WIDTH,
                         MainWindowGeometry.HEIGHT)

    def update_video(self, screen_capture):
        frame = QImage(screen_capture.data,
                       screen_capture.shape[1],
                       screen_capture.shape[0],
                       QImage.Format_RGB888)

        self.window.video_lb.setPixmap(QPixmap.fromImage(frame))


class VideoThread(QThread):  # 线程类
    screen_capture_signal = pyqtSignal(np.ndarray)  # 自定义信号对象。参数str就代表这个信号可以传一个字符串

    def __init__(self):
        super(VideoThread, self).__init__()

    def run(self):  # 线程执行函数
        while True:
            video_info = engine.video_info
            if video_info is not None:
                screen_capture = engine.video_info[Common.KEY_SCREEN_CAPTURE]
                if screen_capture is not None:
                    self.screen_capture_signal.emit(screen_capture)  # 释放自定义的信号
            # 通过自定义信号把video_info传递给槽函数
            self.msleep(100)  # 本线程睡眠n毫秒
