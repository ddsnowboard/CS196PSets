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
            # self.assertEqual(reverse_string("apples"), "selppa")
            # self.assertEqual(reverse_string("apple"), "elppa")
            # self.assertEqual(reverse_string("Hello World", "dlroW olleH"))

        def test_oddEven(self):
            # self.assertEqual("odd", oddEven("one"))
            # self.assertEqual("even", oddEven("four"))

        def test_sign_flipper(self):
            pass
