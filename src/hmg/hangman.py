import random

from hmg.display import clean_screen, draw_header


words = ["aback"]


class Hangman():
    def __init__(self, char_tablero='-', nombre_jugador='player_default'):
        self.nombre_jugador = nombre_jugador
        self.palabra_secreta = get_word(words)
        self.letras_palabra_secreta = set(self.palabra_secreta)
        self.letras_usadas = set()
        self.char_tablero = char_tablero
        self.tablero = [self.char_tablero for _ in range(len(self.palabra_secreta))]
        self.vidas = 5

    def letra_is_valid(self, letra):
        letra_valid = True
        if letra.isdigit() or not letra:
            letra_valid = False
        return letra_valid

    def pedir_letra(self, msg=''):
        return input(f'Ingresa una letra{msg}: ')

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
        while len(self.letras_palabra_secreta) > 0 and self.vidas > 0:
            # print(self.tablero)
            draw_header(self.tablero, self.letras_usadas, self.vidas)

            letra_ingresada = self.pedir_letra().upper()
            if not self.letra_is_valid(letra_ingresada):
                print('Por favor ingresa una letra valida\n')
                continue

            for _ in range(self.palabra_secreta.count(letra_ingresada)):
                index = self.palabra_secreta.index(letra_ingresada)
                self.palabra_secreta.pop(index)
                self.palabra_secreta.insert(index, self.char_tablero)
                self.tablero.pop(index)
                self.tablero.insert(index, letra_ingresada)

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
    return list(word.upper())
