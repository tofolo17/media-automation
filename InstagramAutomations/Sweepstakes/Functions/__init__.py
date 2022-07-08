from random import randint
from time import sleep
from tkinter import *

import pyautogui as pg


def vai_e_clica(xy: tuple):
    pg.moveTo(xy[0], xy[1], randint(50, 100) / 100)
    pg.click(button='left')


def randomiza(x, y):
    return x + (randint(-100, 100) / 1000), y + (randint(-100, 100) / 1000),


def vai_e_segura(xy: tuple):
    pg.moveTo(xy[0], xy[1], randint(50, 100) / 100)
    pg.mouseDown(button='left')
    sleep(1)
    pg.mouseUp(button='left')


def scroll(xy: tuple):
    pg.mouseDown(button='left')
    pg.moveTo(xy[0], xy[1], 1)
    pg.mouseUp(button='left')


def verifica_bloqueio(xy: tuple):
    pg.moveTo(xy[0], xy[1], randint(50, 75) / 100)
    pg.mouseDown(button='left')
    pg.moveTo(xy[0] + 200, xy[1], randint(50, 75) / 100)
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
