""" tests for module word_utils """

import unittest
from unittest import mock

from hmg.word_utils import (
    get_word_from_internet,
    normalize_word,
)


class WordUtilsTestCase(unittest.TestCase):
    @mock.patch("hmg.word_utils.requests.get")
    def test_word_from_interent(self, mock_get):
        fake_response = {"body": {"Word": "mipalabra"}}
        expected = "mipalabra"

        mock_get.return_value.json.return_value = fake_response
        word = get_word_from_internet()

        self.assertEqual(word, expected)

    @mock.patch("hmg.word_utils.requests.get")
    def test_separate_word(self, mock_get):
        fake_response = {"body": {"Word": "oso pardo"}}
        expected = "oso"

        mock_get.return_value.json.return_value = fake_response
        word = get_word_from_internet()

        self.assertEqual(word, expected)

    @mock.patch("hmg.word_utils.requests.get")
    def test_get_word_and_normalize(self, mock_get):
        fake_response = {"body": {"Word": "espátula"}}
        expected = "espatula"

        mock_get.return_value.json.return_value = fake_response
        word = get_word_from_internet()

        self.assertEqual(word, expected)

    def test_normalize_word(self):
        words = ["espátula", "constitución", "áéiiíóÚ"]
        normalized_words = ["espatula", "constitucion", "aeiiioU"]

        for word, normalized_word in zip(words, normalized_words):
            w = normalize_word(word)
            self.assertEqual(w, normalized_word)
