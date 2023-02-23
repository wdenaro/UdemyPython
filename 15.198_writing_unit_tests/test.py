import unittest
import script


class TestMain(unittest.TestCase):

    def test_with_integer(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_with_string(self):
        test_param = 'qwerty'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_with_empty_string(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'parameter must be a number')

    def test_with_none(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'parameter must be a number')

    def test_with_float(self):
        test_param = 3.14159
        result = script.do_stuff(test_param)
        self.assertFalse(isinstance(result, ValueError))

    def test_with_list(self):
        test_param = ['w', 'd']
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, TypeError))


if __name__ == '__main__':
    unittest.main()
