import unittest
from unittest_practice import add, is_even

class test_functions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2), 3)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))

if __name__ == "__main__":
    unittest.main()