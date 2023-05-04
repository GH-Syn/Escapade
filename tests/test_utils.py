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



if __name__ == "__main__":
    unittest.main()
