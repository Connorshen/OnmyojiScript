from static import config
from os import path


class ImageKey:
    KEY_CHALLENGE = "挑战"
    KEY_MITAMA = "御魂"
    KEY_AWAKEN = "觉醒"


class ResUrl:
    ROOT_DIR = config.RES_PATH
    HOMEPAGE_PATH = path.join(ROOT_DIR, "homepage")
    SHIKIGAMI_PATH = path.join(HOMEPAGE_PATH, "Shikigami.png")  # 式神录

    EXPLORE_PATH = path.join(ROOT_DIR, "explore")  # 御魂
    CHALLENGE_PATH = path.join(EXPLORE_PATH, "Challenge.png")  # 挑战
    MITAMA_PATH = path.join(EXPLORE_PATH, "Mitama.png")  # 御魂
    AWAKEN_PATH = path.join(EXPLORE_PATH, "Awaken.png")  # 觉醒材料

    HOME_ALL = [SHIKIGAMI_PATH]
    MIKUN_ALL = {ImageKey.KEY_CHALLENGE: CHALLENGE_PATH,
                 ImageKey.KEY_MITAMA: MITAMA_PATH,
                 ImageKey.KEY_AWAKEN: AWAKEN_PATH}
