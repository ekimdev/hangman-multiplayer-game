""" tests for module hangman. """

import unittest
from unittest import mock

from hmg.hangman import Hangman


class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Hangman("mipalabra")

    def test_letras_in_palabra(self):
        expected = set(self.player.palabra_secreta)

        self.assertSetEqual(self.player.letras_palabra_secreta, expected)

    def test_letra_is_valid(self):
        with mock.patch("builtins.input", return_value="a"):
            letra_ingresada = self.player.pedir_letra()

            self.assertTrue(self.player.letra_is_valid(letra_ingresada))

    def test_pedir_letra_is_num(self):
        with mock.patch("builtins.input", return_value="2"):
            letra_ingresada = self.player.pedir_letra()

            self.assertFalse(self.player.letra_is_valid(letra_ingresada))

    def test_pedir_letra_is_empty(self):
        with mock.patch("builtins.input", return_value=""):
            letra_ingresada = self.player.pedir_letra()

            self.assertFalse(self.player.letra_is_valid(letra_ingresada))
