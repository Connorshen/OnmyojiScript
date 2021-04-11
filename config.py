import os, sys


class Config:
    ROOT = None

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.ROOT = os.path.dirname(sys.executable)
        elif __file__:
            self.ROOT = os.path.dirname(__file__)
        self.VALIDATION_REQUIRED = []
        self.verify_path()

    def verify_path(self):
        for filepath in self.VALIDATION_REQUIRED:
            if os.path.exists(filepath) is not True:
                os.mkdir(filepath)
