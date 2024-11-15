# test_add.py
import unittest
from add import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        # Test addition functionality
        self.assertEqual(add(3, 7), 10)  # Positive numbers
        self.assertEqual(add(-1, 1), 0)  # Positive and negative
        self.assertEqual(add(-1, -1), -2)  # Negative numbers

if _name_ == '_main_':
    unittest.main()
