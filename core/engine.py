import cv2
from PyQt5.QtCore import QThread, pyqtSignal

from config import Common
from res.url import ResUrl, Scene
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

    @staticmethod
    def get_scene_similarity(find_result, templates):
        # 识别场景
        templates_len = len(templates)
        templates_find_len = 0
        for key in find_result.keys():
            if key in templates.keys():
                templates_find_len += 1
        scene_similarity = templates_find_len / templates_len
        return scene_similarity

    def reg_scene(self, find_result):
        scenes_similarity = []
        for key_scene in ResUrl.ALL:
            scenes_path = ResUrl.ALL[key_scene]
            scene_similarity = self.get_scene_similarity(find_result, scenes_path)
            scenes_similarity.append([key_scene, scene_similarity])
        scenes_similarity = sorted(scenes_similarity, key=lambda x: (x[1]), reverse=True)
        max_scene_name = scenes_similarity[0][0]
        max_scene_similarity = scenes_similarity[0][1]
        if max_scene_similarity > config.SCENE_SIMILARITY_THRESHOLD:
            return max_scene_name
        else:
            return Scene.OTHER

    def run(self):  # 线程执行函数
        while True:
            video_info = engine.video_info  # 释放自定义的信号
            screen_capture = video_info[Common.KEY_SCREEN_CAPTURE]
            if screen_capture is not None:
                screen_capture = screen_capture.copy()
                # TODO 扩展功能，目前只写刷御魂
                find_result = {}
                need_paint_rect_points = []
                for key_scene in ResUrl.ALL:
                    scenes_path = ResUrl.ALL[key_scene]
                    for key_template in ResUrl.ALL[key_scene]:
                        file_path = scenes_path[key_template]
                        template = cv2.imread(file_path, 0)
                        find_flag, left_top, right_bottom = reg_template(screen_capture, template)
                        if find_flag:
                            find_result[key_template] = {"left_top": left_top,
                                                         "right_bottom": right_bottom}
                            need_paint_rect_points.append([left_top, right_bottom])
                # 画红框，标记模板
                for left_top, right_bottom in need_paint_rect_points:
                    cv2.rectangle(screen_capture, tuple(left_top), tuple(right_bottom), (255, 0, 0), 2)
                self.reg_info[Common.KEY_REG_SCENE] = self.reg_scene(find_result)
                self.reg_info[Common.KEY_REG_IMAGE] = screen_capture
                self.reg_info[Common.KEY_REG_FIND] = find_result
            self.msleep(config.REG_INTERVAL_TIME)  # 本线程睡眠n毫秒


engine = Engine()
