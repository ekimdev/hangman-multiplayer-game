import random


words = ["aback"]


class Hangman():
    def __init__(self, nombre_jugador='player_default'):
        self.nombre_jugador = nombre_jugador
        self.palabra_secreta = get_word(words)
        self.letras_palabra_secreta = set(self.palabra_secreta)
        self.letras_usadas = set()
        self.tablero = ["_" for _ in range(len(self.palabra_secreta))]
        self.vidas = 5

    def letra_is_valid(self, letra):
        letra_valid = True
        if letra.isdigit() or not letra:
            letra_valid = False
        return letra_valid

    def pedir_letra(self):
        return input('Ingresa una letra: ')

    def comprobar_letras_usadas(self, letra_ingresada):
        if letra_ingresada not in self.letras_usadas:
            self.letras_usadas.add(letra_ingresada)
        else:
            print(f'Ya ingresaste la letra {letra_ingresada}')

    def terminar_juego(self):
        if self.vidas == 0:
            print('Se acabo el juego, Perdiste!!')
        else:
            print('Ganaste!!')

    def start_game(self):
        while self.vidas > 0:
            print(self.tablero)

            letra_ingresada = self.pedir_letra()
            if not self.letra_is_valid(letra_ingresada):
                letra_ingresada = self.pedir_letra() + 'Valida'
            self.comprobar_letras_usadas(letra_ingresada)
            if letra_ingresada in self.letras_palabra_secreta:
                self.letras_palabra_secreta.remove(letra_ingresada)
            else:
                self.vidas = self.vidas - 1

        self.terminar_juego()

def get_word(archivo):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
