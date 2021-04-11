from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow

from config import Common, MainWindowGeometry
from core.engine import engine
from view.design.main_window import Ui_MainWindow
import cv2


class MainWindowView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.init_widget()
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.update_video)
        self.video_timer.start(10)
        engine.start_capture()

    def init_widget(self):
        self.setGeometry(MainWindowGeometry.X,
                         MainWindowGeometry.Y,
                         MainWindowGeometry.WIDTH,
                         MainWindowGeometry.HEIGHT)

    def update_video(self):
        video_info = engine.video_info
        if video_info is not None:
            screen_capture = video_info[Common.KEY_SCREEN_CAPTURE]
            if screen_capture is not None:
                screen_capture = cv2.resize(screen_capture, (0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_NEAREST)
                frame = QImage(screen_capture.data,
                               screen_capture.shape[1],
                               screen_capture.shape[0],
                               screen_capture.shape[1] * 3,
                               QImage.Format_RGB888)
                self.window.video_lb.setPixmap(QPixmap.fromImage(frame))
                self.window.recognition_lb.setPixmap(QPixmap.fromImage(frame))
                self.window.left_lb.setText(str(video_info[Common.KEY_VIDEO_LEFT]))
                self.window.right_lb.setText(str(video_info[Common.KEY_VIDEO_RIGHT]))
                self.window.top_lb.setText(str(video_info[Common.KEY_VIDEO_TOP]))
                self.window.bottom_lb.setText(str(video_info[Common.KEY_VIDEO_BOTTOM]))
                self.window.height_lb.setText(str(video_info[Common.KEY_VIDEO_LEFT]))
                self.window.width_lb.setText(str(video_info[Common.KEY_VIDEO_WIDTH]))
