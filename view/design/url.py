# -*- coding: utf-8 -*-
"""
@Time    : 2019-07-07 12:26
@Author  : 比尔丶盖子
@Email   : 914138410@qq.com
"""
import os


class Config:
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    UI_PATH = os.path.join(ROOT_DIR, "ui")
    PY_PATH = ROOT_DIR
