import random

import pyautogui
from PyQt5.QtCore import QThread

from config import Common
from core.engine import engine
from core.log import log
from res.url import Scene, ImageKey
from static import config
from util import send_message


class BrushMitamaThread(QThread):
    def __init__(self):
        super(BrushMitamaThread, self).__init__()
        self.is_running = True

    def normal_click(self, image_key, find_result):
        if image_key in find_result.keys():
            btn = find_result[image_key]
            self.single_click(btn)

    def stop(self):
        self.is_running = False

    def shift_y_click(self, image_key, find_result, shift):
        if image_key in find_result.keys():
            btn = find_result[image_key]
            # 位移
            btn["left_top"][1] += shift
            btn["right_bottom"][1] += shift
            # 点击
            self.single_click(btn)

    def single_click(self, btn):
        left_top = btn["left_top"]
        right_bottom = btn["right_bottom"]
        left = left_top[0]
        top = left_top[1]
        right = right_bottom[0]
        bottom = right_bottom[1]
        # 计算中间点
        mid_x = random.randint(left, right)
        mid_y = random.randint(top, bottom)
        # 移动并点击
        self.move_and_click(mid_x, mid_y)

    def random_move(self, width, height):
        # 随机时间位移
        x = random.randint(0, width)
        y = random.randint(100, height - 100)
        pyautogui.moveTo(x, y, duration=random.randint(1, config.RANDOM_SHIFT_TIME))

    def move_and_click(self, x, y):
        # 随机时间位移
        pyautogui.moveTo(x, y, duration=random.randint(1, config.RANDOM_SHIFT_TIME))
        pyautogui.click()

    @staticmethod
    def left_drag(width, height):
        # 计算中间点
        mid_x = width / 2
        mid_y = height / 2
        mid_y += 60
        start_x = mid_x + 100
        end_x = mid_x - 100
        pyautogui.moveTo(start_x, mid_y, duration=random.randint(1, config.RANDOM_SHIFT_TIME))
        pyautogui.dragTo(end_x, mid_y, duration=random.randint(1, config.RANDOM_SHIFT_TIME), button='left')

    def run(self):  # 线程执行函数
        log.print("开始执行脚本")
        execution_times = 0
        while self.is_running:
            reg_info = engine.reg_info
            video_info = engine.video_info
            scene = reg_info[Common.KEY_REG_SCENE]
            width = video_info[Common.KEY_VIDEO_WIDTH]
            height = video_info[Common.KEY_VIDEO_HEIGHT]
            find_result = reg_info[Common.KEY_REG_FIND]

            if scene == Scene.HOMEPAGE:
                if ImageKey.KEY_EXPLORE not in find_result.keys():
                    self.left_drag(width, height)
                    log.print("主页左移")
                else:
                    self.normal_click(ImageKey.KEY_EXPLORE, find_result)
            if scene == Scene.EXPLORE:
                self.normal_click(ImageKey.KEY_MITAMA, find_result)
                log.print("点击御魂按钮")
            if scene == Scene.MITAMA:
                self.normal_click(ImageKey.KEY_EIGHT_SNAKE, find_result)
                log.print("点击八岐大蛇")
            if scene == Scene.MITAMA_DETAIL:
                self.normal_click(ImageKey.KEY_CHALLENGE, find_result)
                log.print("点击挑战")
            if scene == Scene.BATTLE:
                self.random_move(width, height)
                log.print("战斗中，随机位移")
            if scene == Scene.BATTLE_END1:
                self.shift_y_click(ImageKey.KEY_BATTLE_END1_THREE, find_result, 40)
                log.print("点击战斗结束1")
            if scene == Scene.BATTLE_END2:
                self.normal_click(ImageKey.KEY_BLESS_BAG, find_result)
                execution_times += 1
                if execution_times >= config.EXECUTION_TIMES:
                    self.stop()
                    log.print("到达执行次数")
                log.print("点击战斗结束2，福袋")
                log.print("执行次数：" + str(execution_times))
            sleep_time = random.randint(1000, config.ACTION_INTERVAL_TIME)
            log.print("当前场景：{0}；脚本防检测，随机暂停{1}毫秒".format(scene, sleep_time))
            self.msleep(sleep_time)
        send_message("御魂脚本运行结束", "御魂战斗次数：" + str(execution_times))
        log.print("脚本运行结束")
