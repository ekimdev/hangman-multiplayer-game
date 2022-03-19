""" tests for module hangman. """

import unittest
from unittest import mock

from hmg.hangman import Hangman


class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Hangman("mipalabra")

    def test_letra_is_valid(self):
        user_input = "a"
        self.assertTrue(self.player.letra_is_valid(user_input))

    def test_letra_is_not_valid_empty_char(self):
        user_input = ""
        self.assertFalse(self.player.letra_is_valid(user_input))

    def test_letra_is_not_valid_number(self):
        user_input = "1"
        self.assertFalse(self.player.letra_is_valid(user_input))

    def test_letras_in_palabra(self):
        expected = set(self.player.palabra_secreta)

        self.assertSetEqual(self.player.letras_palabra_secreta, expected)

    def test_pedir_letra(self):
        invalid_inputs = [" ", "1", "    ", "a"]
        with mock.patch("builtins.input", side_effect=invalid_inputs) as mock_input:
            self.player.pedir_letra()

            # Check que input se ha llamado 3 veces (a b y c)
            self.assertEqual(mock_input.call_count, 4)
