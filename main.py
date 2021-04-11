import win32gui, win32ui, win32con
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

def get_windows(windowsname, filename):
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, windowsname)
    # 将窗口放在前台，并激活该窗口（窗口不能最小化）
    win32gui.SetForegroundWindow(handle)
    # 获取窗口DC
    hdDC = win32gui.GetWindowDC(handle)
    # 根据句柄创建一个DC
    newhdDC = win32ui.CreateDCFromHandle(hdDC)
    # 创建一个兼容设备内存的DC
    saveDC = newhdDC.CreateCompatibleDC()
    # 创建bitmap保存图片
    saveBitmap = win32ui.CreateBitmap()

    # 获取窗口的位置信息
    left, top, right, bottom = win32gui.GetWindowRect(handle)
    # 窗口长宽
    width = right - left
    height = bottom - top
    # bitmap初始化
    saveBitmap.CreateCompatibleBitmap(newhdDC, width, height)
    saveDC.SelectObject(saveBitmap)
    saveDC.BitBlt((0, 0), (width, height), newhdDC, (0, 0), win32con.SRCCOPY)
    saveBitmap.SaveBitmapFile(saveDC, filename)


get_windows("GitHub", "截图.png")
