""" tests for module hangman. """

import unittest
from unittest import mock

from hmg.hangman import Hangman
from hmg.hangman import get_word, words


class HangmanTestCase(unittest.TestCase):
    def test_obtener_palabra(self):
        palabra = "aback".upper()
        expected = get_word(words)

        self.assertEqual("".join(expected), palabra)

    def test_letras_in_palabra(self):
        player = Hangman()
        expected = set(player.palabra_secreta)

        self.assertSetEqual(player.letras_palabra_secreta, expected)

    def test_letra_is_valid(self):
        player = Hangman()
        with mock.patch("builtins.input", return_value="a"):
            letra_ingresada = player.pedir_letra()

            self.assertTrue(player.letra_is_valid(letra_ingresada))

    def test_pedir_letra_is_num(self):
        player = Hangman()
        with mock.patch("builtins.input", return_value="2"):
            letra_ingresada = player.pedir_letra()

            self.assertFalse(player.letra_is_valid(letra_ingresada))

    def test_pedir_letra_is_empty(self):
        player = Hangman()
        with mock.patch("builtins.input", return_value=""):
            letra_ingresada = player.pedir_letra()

            self.assertFalse(player.letra_is_valid(letra_ingresada))
