import os
import sys


class Config:
    ROOT = None

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.ROOT = os.path.dirname(sys.executable)
        elif __file__:
            self.ROOT = os.path.dirname(__file__)
        self.TEMPLATE_SIMILARITY_THRESHOLD = 0.7  # 模板相似度，大于这个就判断为相似
        self.SCENE_SIMILARITY_THRESHOLD = 0.2  # 场景相似度，即10个模板有5个匹配就判定为相似
        self.RANDOM_SHIFT_PIXEL = 10  # 识别出模板后，按中间点(x,y)随机产生位移的像素值
        self.RANDOM_SHIFT_TIME = 1  # 鼠标移动的时间
        self.CAPTURE_INTERVAL_TIME = 10  # 捕获图像的时间间隔，毫秒
        self.REG_INTERVAL_TIME = 10  # 识别图像的时间间隔，毫秒
        self.ACTION_INTERVAL_TIME = 5000  # 行动时间间隔，毫秒
        self.LOG_SCREEN_LEN = 20  # 屏幕最多显示的Log条数
        self.RES_PATH = os.path.join(self.ROOT, "res")
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
        self.REG_INFO_INIT = {
            Common.KEY_REG_IMAGE: None,
            Common.KEY_REG_FIND: {},
            Common.KEY_REG_SCENE: ""
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

    KEY_REG_IMAGE = "reg_image"
    KEY_REG_FIND = "reg_find"
    KEY_REG_SCENE = "reg_scene"
