import keyboard
import pyautogui

while True:
    keyboard.wait("SPACE")
    x, y = pyautogui.position()
    print(x, y)
    with open('text/coordenadas', 'a') as f:
        f.write(f'{x} {y}\n')
