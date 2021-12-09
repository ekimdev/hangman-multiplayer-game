
class Game:
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
