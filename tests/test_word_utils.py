""" tests for module word_utils """

import unittest
from unittest import mock

from hmg.word_utils import get_word_from_internet


class WordUtilsTestCase(unittest.TestCase):
    @mock.patch("hmg.word_utils.requests.get")
    def test_word_from_interent(self, mock_get):
        fake_response = {"body": {"Word": "mipalabra"}}
        expected = "mipalabra"

        mock_get.return_value.json.return_value = fake_response
        word = get_word_from_internet()

        self.assertEqual(word, expected)
