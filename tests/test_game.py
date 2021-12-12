"""" tests for module game. """
import unittest
from unittest import mock

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

    def test_choose_option_one(self):
        game = Game()
        with mock.patch('builtins.input', return_value=1):
            option = game.choose_option()
            expected = game.OPTION_ONE_PLAYER
            self.assertEqual(option, expected)

    def test_choose_option_two(self):
        game = Game()
        with mock.patch('builtins.input', return_value=2):
            option = game.choose_option()
            expected = game.OPTION_TWO_PLAYERS
            self.assertEqual(option, expected)

    def test_choose_option_three(self):
        game = Game()
        with mock.patch('builtins.input', return_value=3):
            option = game.choose_option()
            expected = game.OPTION_EXIT
            self.assertEqual(option, expected)

    def test_choose_invalid_option(self):
        game = Game()
        with mock.patch('builtins.input', return_value='1'):
            option = game.choose_option()
            expected = game.OPTION_ONE_PLAYER
            self.assertEqual(option, expected)
