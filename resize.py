import pyautogui

def resize_t():
    windows = pyautogui.getWindowsWithTitle("Windows PowerShell")
    if windows:
        print("Found Windows PowerShell window, resizing...")
        windows[0].resizeTo(848, 525)
    else:
        print("No Windows PowerShell window found.")
        windows = pyautogui.getWindowsWithTitle("cmd")
        windows[0].resizeTo(848, 525)
     
resize_t()