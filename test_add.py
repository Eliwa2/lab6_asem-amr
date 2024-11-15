# test_add.py
import unittest
from add import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        # Test addition functionality
        result = add(3, 7)
        self.assertEqual(result, 10)
        
        result = add(-1, 1)
        self.assertEqual(result, 0)
        
        result = add(-1, -1)
        self.assertEqual(result, -2)

if _name_ == '_main_':
    unittest.main()
