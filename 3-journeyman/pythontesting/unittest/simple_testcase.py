import unittest

class Testing(unittest.TestCase):
    #test if 2 strings are equal
    def test_string(self):
        x = 'alpha'
        y = 'alpha'
        self.assertEqual(x, y)

if __name__ == '__main__':

    unittest.main()