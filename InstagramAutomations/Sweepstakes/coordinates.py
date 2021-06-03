import keyboard
import pyautogui

while True:
    keyboard.wait("SPACE")
    x, y = pyautogui.position()
    print(x, y)
    with open('Data/coordenadas', 'a') as f:
        f.write(f'{x} {y}\n')
