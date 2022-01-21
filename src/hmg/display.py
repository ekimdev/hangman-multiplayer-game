import os
import sys


def clean_screen():
    comando = 'clear'

    if sys.platform == 'windows':
        comando = 'cls'

    os.system(comando)


def draw_board(tablero):
    print(''.join(tablero), end='')


def draw_header(tablero, letras_usadas, vidas, juego):
    draw_board(tablero)
    print(' ' * 20, end='')
    print(f'Letras usadas: {letras_usadas}', end='')
    print(' ' * 20, end='')
    print(f'Vidas: {vidas}', end='')
    print(' ' * 20, end='')
