import os
import sys

from hmg import __version__


def clean_screen():
    comando = "clear"

    if sys.platform == "windows":
        comando = "cls"

    os.system(comando)


def draw_board(tablero):
    print("".join(tablero).upper(), end="")


def draw_header(tablero, letras_usadas, vidas):
    draw_board(tablero)
    print(" " * 20, end="")
    used_letter_board = ",".join(letras_usadas).upper()
    print(f"Letras usadas: {used_letter_board}", end="")
    print(" " * 20, end="")
    print(f"Vidas: {vidas}", end="")
    print(" " * 20, end="")
    print(f"[version={__version__}]", end="\n" * 5)
