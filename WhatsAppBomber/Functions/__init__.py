from time import sleep

import pyautogui

from Utils import get_url_text


def send_image():
    j = 0
    while j < 3:
        i = 0
        while i < 20:
            pyautogui.hotkey('ctrl', 'v')
            sleep(0.5)
            i += 1
        pyautogui.press('enter')
        j += 1


def send_book():
    book_text = get_url_text("https://www.gutenberg.org/files/30107/30107-h/30107-h.html")
    print(book_text)
    for word in book_text.split():
        pyautogui.typewrite(word)
        pyautogui.press('enter')
