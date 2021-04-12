from static import config
from os import path
from util import merge_dicts


class ImageKey:
    KEY_SHIKIGAMI = "式神录"
    KEY_EXPLORE = "探索"
    KEY_EMAIL = "邮箱"
    KEY_CHAT = "聊天"

    KEY_CHALLENGE = "挑战"
    KEY_MITAMA = "御魂"
    KEY_AWAKEN = "觉醒"


class ResUrl:
    ROOT_DIR = config.RES_PATH
    HOMEPAGE_PATH = path.join(ROOT_DIR, "homepage")
    SHIKIGAMI_PATH = path.join(HOMEPAGE_PATH, "Shikigami.png")  # 式神录
    EXPLORE_PATH = path.join(HOMEPAGE_PATH, "Explore.png")  # 探索
    EMAIL_PATH = path.join(HOMEPAGE_PATH, "Email.png")  # 邮箱
    CHAT_PATH = path.join(HOMEPAGE_PATH, "Chat.png")  # 聊天

    EXPLORE_PAGE_PATH = path.join(ROOT_DIR, "explore")  # 御魂
    CHALLENGE_PATH = path.join(EXPLORE_PAGE_PATH, "Challenge.png")  # 挑战
    MITAMA_PATH = path.join(EXPLORE_PAGE_PATH, "Mitama.png")  # 御魂
    AWAKEN_PATH = path.join(EXPLORE_PAGE_PATH, "Awaken.png")  # 觉醒材料

    HOME_ALL = {ImageKey.KEY_SHIKIGAMI: SHIKIGAMI_PATH,
                ImageKey.KEY_EXPLORE: EXPLORE_PATH,
                ImageKey.KEY_EMAIL:EMAIL_PATH,
                ImageKey.KEY_CHAT:CHAT_PATH}
    MIKUN_ALL = {ImageKey.KEY_CHALLENGE: CHALLENGE_PATH,
                 ImageKey.KEY_MITAMA: MITAMA_PATH,
                 ImageKey.KEY_AWAKEN: AWAKEN_PATH}

    ALL = merge_dicts([HOME_ALL, MIKUN_ALL])
