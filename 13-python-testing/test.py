import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test function")

    def test_do_stuff(self):
        '''Simple math test'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''Simple string test'''
        test_param = "sd561sdf651"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''Simple None test'''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please Enter Number")

    def test_do_stuff4(self):
        '''Simple negative value test'''
        test_param = -10
        result = main.do_stuff(test_param)
        self.assertEqual(result, -5)

    def test_do_stuff5(self):
        '''Simple empty string test'''
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please Enter Number")

    def test_do_stuff6(self):
        '''Simple 0 test'''
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please Enter Number")

    def tearDown(self):
        print("Cleaning Up")


if __name__ == "__main__":
    unittest.main()
