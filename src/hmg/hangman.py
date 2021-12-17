import random


words = ["aback"]


class Hangman():
    def __init__(self, nombre_jugador='player_default'):
        self.nombre_jugador = nombre_jugador
        self.palabra_secreta = get_word(words)
        self.letras_palabra_secreta = set(self.palabra_secreta)
        self.vidas = 5

    def letra_is_valid(self, letra):
        letra_valid = True
        if letra.isdigit() or not letra:
            letra_valid = False
        return letra_valid

    def pedir_letra(self):
        return input('Ingresa una letra: ')

def get_word(archivo):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
