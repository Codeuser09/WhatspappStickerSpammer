import win32api, win32con
import random
import keyboard
import time


# x, y point 1: 600, 730
# x, y point 2: 1900, 950on/AI/Whatsapp_StickerSpam.py', wdir='D:/Projekte/Python/AI')


numberKlicks = 0

time.sleep(5)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    


while not keyboard.is_pressed("k"):
    x = 1798
    y = 888
    
    click(x, y)
    numberKlicks += 1
    time.sleep(0.1)