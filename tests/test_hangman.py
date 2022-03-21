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

    def test_pedir_letra_lowercase(self):
        valid_inputs = ["A", "b", "C", "d"]
        expected = ["a", "b", "c", "d"]
        with mock.patch("builtins.input", side_effect=valid_inputs):
            valid_char = self.player.pedir_letra()
            expected_char = expected.pop(0)

            self.assertEqual(valid_char, expected_char)

    def test_char_is_used(self):
        self.player.letras_usadas = set(["a", "b", "c"])
        self.assertTrue(self.player.char_is_used("a"))

    def test_char_is_not_used(self):
        self.player.letras_usadas = set(["a", "b", "c"])
        self.assertFalse(self.player.char_is_used("d"))
