import sys, os
sys.path.insert(0, os.getcwd())
from game.main import *
import unittest


class TestFoo(unittest.TestCase):
    def test_add(self):
        test_data = [(2, 3), (1, 3)]
        
        for group in test_data:
            result = add(*group)
            self.assertEqual(result, group[0] + group[1], "Addition error")

            # Check for the mutated code
            self.assertNotEqual(result, group[0] - group[1], "Subtraction error")

            # Check for None
            self.assertIsNotNone(result, "None returned")
