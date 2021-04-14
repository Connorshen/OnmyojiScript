# 阴阳师自动肝御魂脚本 (OnmyojiScript)
[![GitHub release](https://img.shields.io/github/release/Connorshen/OnmyojiScript)](https://github.com/Connorshen/OnmyojiScript/releases) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Connorshen/OnmyojiScript)
![GitHub](https://img.shields.io/github/license/Connorshen/OnmyojiScript)
![platforms](https://img.shields.io/badge/platform-win64-brightgreen.svg)
![GitHub contributors](https://img.shields.io/github/contributors/Connorshen/OnmyojiScript.svg)

还在为体力用不完而发愁吗？还在为樱饼有限而苦难吗？那就来试试这款阴阳师护肝神器吧，本工具专为各位阴阳师
大佬研发，一键刷御魂，解放你的双手。如有疑问可以加QQ群：281409528，或者发邮件至billshen1995@gmail.com

# 运行截图 (Screenshot)
<img src="http://qrjumbyu2.hn-bkt.clouddn.com/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE.png" width = "400" />

# 运行环境 (Environment)
|  环境    | 版本  |
|  :----:  | :----:  |
|  Python解释器 | 3.6  |
| 模拟器  | MuMu模拟器 |
| 系统  | Windows10，64位 |
# 使用方法 (Instruction)
1. 下载可执行文件[OnmyojiScript_win64](https://github.com/Connorshen/OnmyojiScript/releases) ，解压文件到任意位置
2. 打开[MuMu模拟器](https://mumu.163.com/) ，打开阴阳师。手动选定阵容并锁定，刷一把八岐大蛇，要确定能稳过。
3. 在阴阳师主页或者探索页面打开本脚本，填写需要刷的次数后点击开始或者按F1运行脚本。
4. 不想刷了点击结束或者按F12结束运行
# 配置说明 (Configuration)
1. 本代码使用[虾推啥](http://www.xtuis.cn/) 作为通知工具，在微信公众号中搜索【虾推啥】，进入公众号后获取Token
，把Token填入脚本程序。脚本运行结束之后会往微信发通知消息。
2. 刷御魂的次数填30次及以下就行，我测试过没问题。
# 技术路线 (Roadmap)
1. 使用pywin32实时截图，存储在内存里
2. 使用opencv查找模板图，模板图事先截取自模拟器，用于场景判断和点击坐标确认
3. 防封手段采用点击操作增加随机时间间隔，点击位置按模板坐标随机确认
4. 使用pyautogui模拟鼠标点击
# 声明 (Statement)
1. 本代码仅供学习交流使用，倒卖脚本等一切盈利手段
2. 写脚本只是为了护肝，代码使用的工具均来自Python开源库，所产生的任何侵权行为与本人无关。
# 协议 (License)

该源代码使用了 [MIT](https://opensource.org/licenses/MIT) 开源协议。

This project is licensed under the [MIT](https://opensource.org/licenses/MIT) license.
# 请作者喝杯茶 (Donation)
- 微信

<img src="http://qrjumbyu2.hn-bkt.clouddn.com/WeChat.png" width = "200" />


- 支付宝

<img src="http://qrjumbyu2.hn-bkt.clouddn.com/AliPay.png" width = "200" />