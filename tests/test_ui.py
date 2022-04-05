""" tests for module ui. """

import unittest
from unittest import mock

from hmg.ui import ask_letter_or_word


class UiTestsCase(unittest.TestCase):
    def test_entered_letter(self):
        invalid_inputs = [" ", "1", "    ", "a"]
        with mock.patch("hmg.ui.Prompt.ask", side_effect=invalid_inputs) as mock_input:
            ask_letter_or_word()

            # Check que input se ha llamado 3 veces (a b y c)
            self.assertEqual(mock_input.call_count, 4)

    def test_entered_letter_lowercase(self):
        valid_inputs = ["A", "b", "C", "d"]
        expected = ["a", "b", "c", "d"]
        with mock.patch("hmg.ui.Prompt.ask", side_effect=valid_inputs):
            valid_char = ask_letter_or_word()
            expected_char = expected.pop(0)

            self.assertEqual(valid_char, expected_char)
