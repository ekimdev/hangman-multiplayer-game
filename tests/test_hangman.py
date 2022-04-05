""" tests for module hangman. """

import unittest

from hmg.hangman import Hangman


class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Hangman("mipalabra")

    def test_letter_is_valid(self):
        user_input = "a"
        self.assertTrue(self.player.letter_is_valid(user_input))

    def test_letter_is_not_valid_empty_char(self):
        user_input = ""
        self.assertFalse(self.player.letter_is_valid(user_input))

    def test_letter_is_not_valid_number(self):
        user_input = "1"
        self.assertFalse(self.player.letter_is_valid(user_input))

    def test_letters_in_word(self):
        expected = set(self.player.secret_word)

        self.assertSetEqual(self.player.secret_word_letters, expected)

    def test_char_is_used(self):
        self.player.letters_used = set(["a", "b", "c"])
        self.assertTrue(self.player.char_is_used("a"))

    def test_char_is_not_used(self):
        self.player.letters_used = set(["a", "b", "c"])
        self.assertFalse(self.player.char_is_used("d"))
