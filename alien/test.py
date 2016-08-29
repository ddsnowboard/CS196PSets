import unittest
class TestSortReverse(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(["ace", "moz", "acdem"], ["a", "c", "d", "e", "m", "o", "z"]) 
