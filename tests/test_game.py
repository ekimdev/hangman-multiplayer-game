"""" tests for module game. """
import unittest

from hmg.game import Game


class GameTestCase(unittest.TestCase):
    def test_build_menu(self):
        nombre_juego = "Hangman"

        expected = (
            f"Bienvenido a {nombre_juego}\n"
            "================================\n\n"
            "1. Jugar\n"
            "2. Reglas\n"
            "3. Salir\n"
        )
        game = Game(nombre_juego)

        self.assertEqual(game.build_menu(), expected)
