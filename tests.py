import ctypes
from random import randint

import keyboard as keyboard
import pyautogui

user32 = ctypes.windll.user32
w, h = user32.GetSystemMetrics(0) // 2, user32.GetSystemMetrics(1) // 2
nw, nh = w, h

v = 1

while True:
    if keyboard.is_pressed("q"):
        break

    if abs(nw - w) > 300 or abs(nh - h) > 300:
        nw, nh = w, h

    r = randint(1, 4)
    if r == 1:
        pyautogui.moveTo(nw + v, nh)
    if r == 1:
        pyautogui.moveTo(nw - v, nh)
    if r == 1:
        pyautogui.moveTo(nw, h + nh)
    if r == 1:
        pyautogui.moveTo(nw, h - nh)
