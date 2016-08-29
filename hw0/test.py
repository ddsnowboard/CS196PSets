import unittest
from hw0 import *

class TestHW0(unittest.TestCase):
    def test_missing_friends(self):
         for i, j in {missing_friends('james', 
                                  '''
                                  james jack jill
                                  jack jill james
                                  jill jack james
                                  '''): 0, 
         
                      missing_friends('james', 
                                  '''
                                  james jack
                                  jack james jill bob
                                  jill jack bob
                                  bob jill jack
                                  '''): 2,
         
                      missing_friends('james', 
                                  '''
                                  james jack
                                  jack james jill
                                  jill jack
                                  '''): 1
                      }.iteritems():
             self.assertEqual(i, j)
    def test_reverse_string(self):
            pass
            # self.assertEqual(reverse_string("apples"), "selppa")
            # self.assertEqual(reverse_string("apple"), "elppa")
            # self.assertEqual(reverse_string("Hello World", "dlroW olleH"))

    def test_oddEven(self):
            pass
            # self.assertEqual("odd", oddEven("one"))
            # self.assertEqual("even", oddEven("four"))

    def test_sign_flipper(self):
            pass
    def test_spiral_matrix(self):
        self.assertEqual(
                spiralMatrix(
                    [["a","b","c","d","e"],
                        ["f","g","h","i","j"],
                        ["k","l","m","n","o"],
                        ["p","q","r","s","t"],
                        ["u","v","w","x","y"]]),
["a","b","c","d","e","j","o","t","y","x","w","v","u","p","k","f","g","h","i","n","s","r","q","l","m"])

        self.assertEqual(
                spiralMatrix(
                    [["a","b","c","d","e", "r"],
                        ["f","g","h","i","j","r"],
                        ["k","l","m","n","o","m"],
                        ["p","q","r","s","t","l"],
                        ["u","v","w","x","y","p"],
                        ["p","w","z","r","v","q"]]),
list("abcderrmlpqvrzwpupkfghijotyxwvqlmnsr"))


if __name__ == '__main__':
    unittest.main()
