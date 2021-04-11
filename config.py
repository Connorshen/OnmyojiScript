import os, sys
from PyQt5.QtWidgets import QApplication


class Config:
    ROOT = None

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.ROOT = os.path.dirname(sys.executable)
        elif __file__:
            self.ROOT = os.path.dirname(__file__)
        self.VALIDATION_REQUIRED = []
        self.verify_path()
        self.VIDEO_INFO_INIT = {
            Common.KEY_VIDEO_LEFT: 0,
            Common.KEY_VIDEO_TOP: 0,
            Common.KEY_VIDEO_RIGHT: 0,
            Common.KEY_VIDEO_BOTTOM: 0,
            Common.KEY_VIDEO_WIDTH: 0,
            Common.KEY_VIDEO_HEIGHT: 0,
            Common.KEY_SCREEN_CAPTURE: None
        }

    def verify_path(self):
        for filepath in self.VALIDATION_REQUIRED:
            if os.path.exists(filepath) is not True:
                os.mkdir(filepath)


class MuMuGeometry:
    X = 0
    Y = 0
    HEIGHT = 450
    WIDTH = 640


class MainWindowGeometry:
    X = MuMuGeometry.X + MuMuGeometry.WIDTH
    Y = 30
    HEIGHT = 720
    WIDTH = 100


class Common:
    KEY_VIDEO_LEFT = "left"
    KEY_VIDEO_RIGHT = "right"
    KEY_VIDEO_TOP = "top"
    KEY_VIDEO_BOTTOM = "bottom"
    KEY_VIDEO_HEIGHT = "height"
    KEY_VIDEO_WIDTH = "width"
    KEY_SCREEN_CAPTURE = "screen_capture"
