import random


words = ["aback", "abaft", "abandoned", "abashed", "aberrant"]


class Hangman():
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.vidas = 5


def get_word(archivo):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
