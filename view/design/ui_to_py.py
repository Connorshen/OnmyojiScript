# -*- coding: utf-8 -*-
"""
@Time    : 2019-07-07 12:24
@Author  : 比尔丶盖子
@Email   : 914138410@qq.com
"""
from view.design.url import Config
import os
from tqdm import tqdm
import sys


def get_all_files(folder):
    """
    递归遍历文件夹下所有文件
    :param folder:
    :return:
    """
    files_ = []
    files = os.listdir(folder)
    for i in range(0, len(files)):
        path = os.path.join(folder, files[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_


def compile_to_py():
    """
    将所有ui文件转换为py
    :return:
    """
    # 编译ui文件
    files = get_all_files(Config.UI_PATH)
    for file in tqdm(files):
        if file.endswith(".ui"):
            _, file_name = os.path.split(file)
            out_file = file_name.split(".")[0] + ".py"
            out_fold = os.path.join(Config.PY_PATH, out_file)
            os.system(sys.executable + " -m PyQt5.uic.pyuic " + file + " -o " + out_fold)
    # 编译资源文件
    os.system("pyrcc5 -o resource_rc.py resource.qrc")


compile_to_py()
