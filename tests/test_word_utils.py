""" tests for module word_utils """
import requests
import unittest
from unittest import mock

from hmg.word_utils import (
    get_word_from_internet,
    normalize_word,
    valid_word,
    get_word_from_alternative_api,
)


class WordUtilsTestCase(unittest.TestCase):
    @mock.patch("hmg.word_utils.requests.get")
    def test_word_from_internet(self, mock_get):
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
    def test_get_word_and_valid_word(self, mock_get):
        fake_response = {"body": {"Word": "e-spá-tula!?"}}
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

    def test_valid_word(self):
        invalid_words = ["esp at-ula", "!!constitucion??", "#ae ii io@U!"]
        valid_words = ["espatula", "constitucion", "aeiiiou"]

        for word, valid_words in zip(invalid_words, valid_words):
            w = valid_word(word)
            self.assertEqual(w, valid_words)

    @mock.patch("hmg.word_utils.get_word_from_alternative_api")
    @mock.patch("hmg.word_utils.requests.get")
    def test_call_alternative_api_when_503(self, mock_get, alternative_mock_get):
        fake_response = requests.models.Response()
        fake_response.status_code = 503

        mock_get.return_value = fake_response
        get_word_from_internet()

        self.assertTrue(alternative_mock_get.called)

    @mock.patch("hmg.word_utils.requests.get")
    def test_word_from_alternative_api(self, mock_get):
        fake_response = [["mi"], ["no"], ["si"], ["palabra"], ["si?"]]
        expected = "palabra"

        mock_get.return_value.json.side_effect = fake_response
        word = get_word_from_alternative_api()

        self.assertTrue(mock_get.call_count, 4)
        self.assertEqual(expected, word)
