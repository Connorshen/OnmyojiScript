from static import config
from os import path


class ImageKey:
    KEY_SHIKIGAMI = "式神录"
    KEY_EXPLORE = "探索"

    KEY_CHALLENGE = "挑战"
    KEY_MITAMA = "御魂"
    KEY_AWAKEN = "觉醒"

    KEY_MITAMA_BACK = "御魂返回"
    KEY_EIGHT_SNAKE = "八岐大蛇"
    KEY_BIG_SNAKE = "巫女大蛇"

    KEY_BATTLE_THREE = "战斗，3个按钮"

    KEY_BATTLE_END1_THREE = "战斗结束1，三个按钮"
    KEY_BATTLE_END2_TWO = "战斗结束2，两个按钮"
    KEY_BLESS_BAG = "福袋"


class Scene:
    HOMEPAGE = "主页"
    EXPLORE = "探索页"
    MITAMA = "御魂"
    MITAMA_DETAIL = "御魂详情"
    BATTLE_END1 = "战斗结束1"
    BATTLE_END2 = "战斗结束2"
    BATTLE = "战斗中"
    OTHER = "未知页面"


class ResUrl:
    ROOT_DIR = config.RES_PATH
    HOMEPAGE_PATH = path.join(ROOT_DIR, "homepage")
    SHIKIGAMI_PATH = path.join(HOMEPAGE_PATH, "Shikigami.png")  # 式神录
    EXPLORE_PATH = path.join(HOMEPAGE_PATH, "Explore.png")  # 探索

    EXPLORE_PAGE_PATH = path.join(ROOT_DIR, "explore")  # 御魂
    CHALLENGE_PATH = path.join(EXPLORE_PAGE_PATH, "Challenge.png")  # 挑战
    MITAMA_PATH = path.join(EXPLORE_PAGE_PATH, "Mitama.png")  # 御魂
    AWAKEN_PATH = path.join(EXPLORE_PAGE_PATH, "Awaken.png")  # 觉醒材料

    MITAMA_PAGE_PATH = path.join(ROOT_DIR, "mitama")
    EIGHT_SNAKE_PATH = path.join(MITAMA_PAGE_PATH, "EightSnake.png")
    MITAMA_BACK_PATH = path.join(MITAMA_PAGE_PATH, "MitamaBack.png")
    BIG_SNAKE_PATH = path.join(MITAMA_PAGE_PATH, "BigSnake.png")
    BATTLE_END_1_PATH = path.join(MITAMA_PAGE_PATH, "BattleEnd1.png")
    BATTLE_END_2_PATH = path.join(MITAMA_PAGE_PATH, "BattleEnd2.png")
    BLESS_BAG_PATH = path.join(MITAMA_PAGE_PATH, "BlessBag.png")
    BATTLE_THREE_BTN_PATH = path.join(MITAMA_PAGE_PATH, "Battle.png")

    HOME_ALL = {ImageKey.KEY_SHIKIGAMI: SHIKIGAMI_PATH,
                ImageKey.KEY_EXPLORE: EXPLORE_PATH}
    EXPLORE_ALL = {ImageKey.KEY_MITAMA: MITAMA_PATH,
                   ImageKey.KEY_AWAKEN: AWAKEN_PATH}
    MITAMA_ALL = {ImageKey.KEY_MITAMA_BACK: MITAMA_BACK_PATH,
                  ImageKey.KEY_EIGHT_SNAKE: EIGHT_SNAKE_PATH}
    MITAMA_DETAIL_ALL = {ImageKey.KEY_MITAMA_BACK: MITAMA_BACK_PATH,
                         ImageKey.KEY_BIG_SNAKE: BIG_SNAKE_PATH,
                         ImageKey.KEY_CHALLENGE: CHALLENGE_PATH}
    BATTLE_END_1_ALL = {ImageKey.KEY_BATTLE_END1_THREE: BATTLE_END_1_PATH}

    BATTLE_END_2_ALL = {ImageKey.KEY_BATTLE_END2_TWO: BATTLE_END_2_PATH,
                        ImageKey.KEY_BLESS_BAG: BLESS_BAG_PATH}

    BATTLE_ALL = {ImageKey.KEY_BATTLE_THREE: BATTLE_THREE_BTN_PATH}

    ALL = {Scene.HOMEPAGE: HOME_ALL,
           Scene.EXPLORE: EXPLORE_ALL,
           Scene.MITAMA: MITAMA_ALL,
           Scene.MITAMA_DETAIL: MITAMA_DETAIL_ALL,
           Scene.BATTLE_END1: BATTLE_END_1_ALL,
           Scene.BATTLE_END2: BATTLE_END_2_ALL,
           Scene.BATTLE: BATTLE_ALL}
