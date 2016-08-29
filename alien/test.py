import unittest
from reverse_sort import *
class TestSortReverse(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_sort(["ace", "moz", "acdem"]), ["a", "c", "d", "e", "m", "o", "z"]) 

if __name__ == "__main__":
    unittest.main()
