from collections import deque
from static import config
import time


class Log:
    def __init__(self):
        self.queue = deque([], maxlen=config.LOG_SCREEN_LEN)

    def print(self, info: str):
        localtime = time.asctime(time.localtime(time.time()))
        self.queue.append(info + "   " + localtime)

    def get_logs(self):
        return list(self.queue)


log = Log()
