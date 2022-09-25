# Rewrite function to use FP
# only test the guessing part

import unittest
import main
from main import answer
from main import guess


class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test function")

    def test_do_stuff(self):
        '''Basic test'''
        test_param = 10
        result = main.guessing_game(test_param)
        self.assertEqual(result, 15)
