from PyQt5.QtWidgets import QMainWindow

from view.design.main_window import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from config import Common, MainWindowGeometry
from core.engine import engine


class MainWindowView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.init_widget()
        engine.start_capture()

    def init_widget(self):
        self.setGeometry(MainWindowGeometry.X,
                         MainWindowGeometry.Y,
                         MainWindowGeometry.WIDTH,
                         MainWindowGeometry.HEIGHT)

    def update_video(self):
        video_info = engine.video_info
        if video_info is not None:
            screen_capture = engine.video_info[Common.KEY_SCREEN_CAPTURE]
