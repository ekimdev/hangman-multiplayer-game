class Hangman:
    def __init__(self, palabra_secreta, char_tablero="-"):
        self.palabra_secreta = list(palabra_secreta)
        self.letras_palabra_secreta = set(self.palabra_secreta)
        self.letras_usadas = set()
        self.char_tablero = char_tablero
        self.tablero = [self.char_tablero for _ in range(len(self.palabra_secreta))]

    @property
    def is_completed(self):
        return self.tablero.count(self.char_tablero) == 0

    def letra_is_valid(self, letra):
        letra_valid = True
        if letra.isdigit() or not letra:
            letra_valid = False
        return letra_valid

    def pedir_letra(self):
        while True:
            user_input = input("Ingresa una letra: ").strip()
            user_input_is_valid = self.letra_is_valid(user_input)
            if user_input_is_valid:
                return user_input.lower()

    def comprobar_letras_usadas(self, letra_ingresada):
        if letra_ingresada not in self.letras_usadas:
            self.letras_usadas.add(letra_ingresada)
        else:
            print(f"Ya ingresaste la letra {letra_ingresada}")

    def letra_esta_en_la_palabra(self, letra_ingresada):
        if letra_ingresada in self.letras_palabra_secreta:
            self.letras_palabra_secreta.remove(letra_ingresada)
            return True
        return False

    def actualizar_tablero(self, letra_ingresada):
        for _ in range(self.palabra_secreta.count(letra_ingresada)):
            index = self.palabra_secreta.index(letra_ingresada)
            self.palabra_secreta.pop(index)
            self.palabra_secreta.insert(index, self.char_tablero)
            self.tablero.pop(index)
            self.tablero.insert(index, letra_ingresada)
