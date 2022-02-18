import unittest
from unittest import mock

from hmg import display


class CleanScreenTestCase(unittest.TestCase):
    @mock.patch("hmg.display.sys.platform", "linux")
    def test_clean_linux(self):
        with mock.patch("os.system") as mock_system:
            display.clean_screen()

            mock_system.assert_called_with("clear")

    @mock.patch("hmg.display.sys.platform", "darwin")
    def test_clean_mac_os(self):
        with mock.patch("os.system") as mock_system:
            display.clean_screen()

            mock_system.assert_called_with("clear")

    @mock.patch("hmg.display.sys.platform", "windows")
    def test_clean_windows(self):

        with mock.patch("os.system") as mock_system:
            display.clean_screen()

            mock_system.assert_called_with("cls")
