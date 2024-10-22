# test_simple_math.py

import unittest
from app import is_even

class TestSimpleMath(unittest.TestCase):

    def test_is_even_with_even_number(self):
        """Test if the function correctly identifies an even number."""
        self.assertTrue(is_even(4))

    def test_is_even_with_odd_number(self):
        """Test if the function correctly identifies an odd number."""
        self.assertFalse(is_even(3))

    def test_is_even_with_zero(self):
        """Test if the function handles zero correctly."""
        self.assertTrue(is_even(0))

if __name__ == '__main__':
    unittest.main()
