import pytest
import utils
import unittest
import os
import sys

sys.path.insert(0, os.getcwd())

from utils import get_display_size


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        kwargs = [
            {"base": True, "display": False, "mixer": True, "font": False},
            {"base": False, "display": False, "mixer": True, "font": False},
            {"base": True, "display": True, "mixer": True, "font": False},
            {"base": True, "display": True, "mixer": True, "font": True},
        ]

        for kwarg in kwargs:
            utils.init(
                init_base=kwarg["base"],
                init_display=kwarg["display"],
                init_mixer=kwarg["mixer"],
                init_font=kwarg["font"],
            )

    @pytest.mark.skipif("DISPLAY" not in os.environ, reason="No display available")
    def test_display_size_valid(self):
        display_size = get_display_size()
        if display_size is not None:  # for no other reason than to make linter happy
            self.assertEqual(display_size[0] % 2, 0)
            self.assertEqual(display_size[1] % 2, 0)

    @pytest.mark.skipif("DISPLAY" not in os.environ, reason="No display available")
    def test_display_size_not_none(self):
        """[redundant]"""
        display_size = get_display_size()
        print(display_size)
        self.assertIsNotNone(display_size, "display is Null")


if __name__ == "__main__":
    unittest.main()
