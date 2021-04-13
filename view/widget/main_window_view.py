from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
import keyboard
from config import Common, MainWindowGeometry
from core.engine import engine
from view.design.main_window import Ui_MainWindow
import cv2
from core.mitama_job import BrushMitamaThread
from core.log import log


class MainWindowView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.init_widget()
        self.video_timer = QTimer()
        self.video_timer.timeout.connect(self.update_video)
        self.video_timer.start(10)
        self.brush_mitama_thread = BrushMitamaThread()
        self.set_listener()
        engine.start_engine()

    def set_listener(self):
        self.window.start_btn.clicked.connect(self.start_brush)
        self.window.end_btn.clicked.connect(self.stop_brush)
        keyboard.add_hotkey('f1', self.start_brush)
        keyboard.add_hotkey('f12', self.stop_brush)

    def start_brush(self):
        self.brush_mitama_thread = BrushMitamaThread()
        self.brush_mitama_thread.start()

    def stop_brush(self):
        self.brush_mitama_thread.stop()

    def init_widget(self):
        self.setGeometry(MainWindowGeometry.X,
                         MainWindowGeometry.Y,
                         MainWindowGeometry.WIDTH,
                         MainWindowGeometry.HEIGHT)

    def update_log(self):
        self.window.log_lv.clear()
        for log_info in log.get_logs():
            self.window.log_lv.addItem(str(log_info))
        self.window.log_lv.scrollToBottom()

    def update_video(self):
        video_info = engine.video_info
        reg_info = engine.reg_info
        reg_image = reg_info[Common.KEY_REG_IMAGE]
        if self.brush_mitama_thread.isRunning():
            self.window.is_running_lb.setText("脚本运行中")
        else:
            self.window.is_running_lb.setText("脚本停止")
        self.update_log()
        if video_info is not None:
            self.window.left_lb.setText(str(video_info[Common.KEY_VIDEO_LEFT]))
            self.window.right_lb.setText(str(video_info[Common.KEY_VIDEO_RIGHT]))
            self.window.top_lb.setText(str(video_info[Common.KEY_VIDEO_TOP]))
            self.window.bottom_lb.setText(str(video_info[Common.KEY_VIDEO_BOTTOM]))
            self.window.height_lb.setText(str(video_info[Common.KEY_VIDEO_HEIGHT]))
            self.window.width_lb.setText(str(video_info[Common.KEY_VIDEO_WIDTH]))
        if reg_image is not None:
            reg_image = cv2.resize(reg_image, (0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_NEAREST)
            frame = QImage(reg_image.data,
                           reg_image.shape[1],
                           reg_image.shape[0],
                           reg_image.shape[1] * 3,
                           QImage.Format_RGB888)
            reg_templates_str = ""
            for key in reg_info[Common.KEY_REG_FIND]:
                reg_templates_str += ("[{}]".format(key))
            self.window.reg_template_lb.setText(reg_templates_str)
            self.window.recognition_lb.setPixmap(QPixmap.fromImage(frame))
            self.window.scene_lb.setText(reg_info[Common.KEY_REG_SCENE])
