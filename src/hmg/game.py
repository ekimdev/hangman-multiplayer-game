
class Game:
    OPTION_ONE_PLAYER = 1
    OPTION_TWO_PLAYERS = 2
    OPTION_EXIT = 3

    def __init__(self, nombre_juego=''):
        self.nombre_juego = nombre_juego

    def build_menu(self):
        menu = (
            f"Bienvenido a {self.nombre_juego}\n"
            "================================\n\n"
            "1. Jugar\n"
            "2. Reglas\n"
            "3. Salir\n"
        )
        return menu

    def choose_option(self):
        menu = self.build_menu()
        print(menu)
        option = 0

        while True:
            try:
                option = int(input('Elige una opcion: '))
            except ValueError:
                print('La opcion no es valida, ingresa de nuevo!')
                print(menu)
                continue
            else:
                if option > 3 or option <= 0:
                    print(menu)
                    continue
                else:
                    break
        return option
