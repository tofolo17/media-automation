from random import randint
from time import sleep
from tkinter import *

import pyautogui as pg


def vai_e_clica(x: int, y: int):
    pg.moveTo(x, y, randint(50, 100) / 100)
    pg.click(button='left')


def vai_e_segura(x: int, y: int):
    pg.moveTo(x, y, randint(50, 100) / 100)
    pg.mouseDown(button='left')
    sleep(1)
    pg.mouseUp(button='left')


def scroll(x: int, y: int):
    pg.mouseDown(button='left')
    pg.moveTo(x, y, 1)
    pg.mouseUp(button='left')


def verifica_bloqueio(x, y):
    pg.moveTo(x, y, randint(50, 75) / 100)
    pg.mouseDown(button='left')
    pg.moveTo(x + 200, y, randint(50, 75) / 100)
    pg.mouseUp(button='left')
    pg.hotkey('ctrl', 'c')

    sleep(1.5)

    try:  # Deve corrigir os erros
        root = Tk()
        root.withdraw()
        valor_copiado = root.clipboard_get()
        root.destroy()
    except TclError:
        valor_copiado = ''
    return valor_copiado


def pegar_contagem(arquivo):
    with open(arquivo, 'r') as f:
        valor = f.read()
    return int(valor)


def atualizar_contagem(arquivo, valor_antigo, soma):
    with open(arquivo, 'w') as f:
        f.write(f'{valor_antigo + soma}')
