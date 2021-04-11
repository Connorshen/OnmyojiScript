from static import config
from os import path


class ResUrl:
    ROOT_DIR = config.RES_PATH
    HOMEPAGE_PATH = path.join(ROOT_DIR, "homepage")
    SHIKIGAMI_PATH = path.join(HOMEPAGE_PATH, "Shikigami.png")  # 式神录

    EXPLORE_PATH = path.join(ROOT_DIR, "explore")  # 御魂
    CHALLENGE_PATH = path.join(EXPLORE_PATH, "Challenge.png")  # 挑战
    MITAMA_PATH = path.join(EXPLORE_PATH, "Mitama.png")  # 御魂
    AWAKEN_PATH = path.join(EXPLORE_PATH, "Awaken.png")  # 觉醒材料

    HOME_ALL = [SHIKIGAMI_PATH]
    MIKUN_ALL = [CHALLENGE_PATH, MITAMA_PATH, AWAKEN_PATH]
