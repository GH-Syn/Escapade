import sys, os
sys.path.insert(0, os.getcwd())
from game.main import *
import unittest



class TestFoo(unittest.TestCase):

    def test_add(self):
        x = 2
        y = 3
        
        result = add(x, y)

        self.assertEqual(result, x + y, "Addition error")

        with self.assertRaises(AssertionError):
            self.assertEqual(result, x - y, "Assertion error expected")
