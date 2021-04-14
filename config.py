import os
import sys
import configparser


class Config:
    ROOT = None

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.ROOT = os.path.dirname(sys.executable)
        elif __file__:
            self.ROOT = os.path.dirname(__file__)
        self.TEMPLATE_SIMILARITY_THRESHOLD = 0.7  # 模板相似度，大于这个就判断为相似
        self.SCENE_SIMILARITY_THRESHOLD = 0.2  # 场景相似度，即10个模板有5个匹配就判定为相似
        self.RANDOM_SHIFT_TIME = 3  # 鼠标移动的时间
        self.REG_INTERVAL_TIME = 10  # 识别图像的时间间隔，毫秒
        self.ACTION_INTERVAL_TIME = 5000  # 行动时间间隔，毫秒
        self.LOG_SCREEN_LEN = 20  # 屏幕最多显示的Log条数
        self.NOTIFY_TOKEN = ""
        self.EXECUTION_TIMES = 0
        self.RES_PATH = os.path.join(self.ROOT, "res")
        self.CONFIG_FILE_PATH = os.path.join(self.RES_PATH, "config.ini")
        self.VALIDATION_REQUIRED = []
        self.verify_path()
        self.VIDEO_INFO_INIT = {
            Common.KEY_VIDEO_LEFT: 0,
            Common.KEY_VIDEO_TOP: 0,
            Common.KEY_VIDEO_RIGHT: 0,
            Common.KEY_VIDEO_BOTTOM: 0,
            Common.KEY_VIDEO_WIDTH: 0,
            Common.KEY_VIDEO_HEIGHT: 0,
            Common.KEY_SCREEN_CAPTURE: None,
            Common.KEY_SIMULATOR_HANDLE: 0
        }
        self.REG_INFO_INIT = {
            Common.KEY_REG_IMAGE: None,
            Common.KEY_REG_FIND: {},
            Common.KEY_REG_SCENE: ""
        }
        self.read_config()
        self.write_config()

    def read_config(self):
        config_parser = configparser.ConfigParser()
        config_parser.read(self.CONFIG_FILE_PATH, encoding="utf-8")
        self.NOTIFY_TOKEN = str(config_parser.get("options", "notify_token"))
        self.EXECUTION_TIMES = int(config_parser.get("options", "execution_times"))

    def write_config(self):
        config_parser = configparser.ConfigParser()
        config_parser.read(self.CONFIG_FILE_PATH, encoding="utf-8")
        config_parser.set("options", "notify_token", self.NOTIFY_TOKEN)
        config_parser.set("options", "execution_times", str(self.EXECUTION_TIMES))
        with open(self.CONFIG_FILE_PATH, "w+") as config_file:
            config_parser.write(config_file)

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
    KEY_SIMULATOR_HANDLE = "simulator_handle"

    KEY_REG_IMAGE = "reg_image"
    KEY_REG_FIND = "reg_find"
    KEY_REG_SCENE = "reg_scene"
