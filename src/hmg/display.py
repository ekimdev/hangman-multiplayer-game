import os
import sys


def clean_screen():
    comando = "clear"

    if sys.platform == "windows":
        comando = "cls"

    os.system(comando)


def draw_board(tablero):
    print("".join(tablero), end="")


def draw_header(tablero, letras_usadas, vidas):
    draw_board(tablero)
    print(" " * 20, end="")
    used_letter_board = ",".join(letras_usadas[1:])
    print(f"Letras usadas: {used_letter_board}", end="")
    print(" " * 20, end="")
    print(f"Vidas: {vidas}", end="\n" * 5)
