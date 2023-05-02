import utils
import unittest
import os
import sys

sys.path.insert(0, os.getcwd())

from utils import get_display_size


class TestUtils(unittest.TestCase):
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

    @unittest.skipIf(
        os.environ.get("DISPLAY") is None, "Skipping test: display not available"
    )
    def test_returns_integers(self):
        size = get_display_size()
        if size is not None:
            self.assertIsInstance(size[0], int)

    @unittest.skipIf(
        os.environ.get("DISPLAY") is None, "Skipping test: display not available"
    )
    def test_returns_non_empty_tuple(self):
        size = get_display_size()
        if isinstance(size, tuple) and (type(size[0]) and type(size[1]) == int):
            self.assertTrue(len(get_display_size()) > 0)  # pyright: ignore

    @unittest.skipIf(
        os.environ.get("DISPLAY") is None, "Skipping test: display not available"
    )
    def test_returns_tuple(self):
        self.assertIsInstance(get_display_size(), tuple)

    @unittest.skipIf(
        os.environ.get("DISPLAY") is None, "Skipping test: display not available"
    )
    def test_returns_valid_size(self):
        size = get_display_size()
        if size is not None:
            width, height = size
            self.assertIsInstance(width, int)
            self.assertIsInstance(height, int)
            self.assertGreater(width, 0)
            self.assertGreater(height, 0)


if __name__ == "__main__":
    unittest.main()
