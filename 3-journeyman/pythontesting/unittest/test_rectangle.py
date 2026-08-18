import unittest
import rectangle_perimeter
import sys

class TestArea(unittest.TestCase):

    # @unittest.skip('Temporarily skips perimeter test') ##Will skip the test and display the string##
    @unittest.skipIf(sys.version_info[0] >= 3,
                     'This test requires Python 2 or lower')
    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 30)

    # def test_error(self):  ##This test passes##
    #     self.assertRaises(ValueError,
    #                       rectangle_perimeter.get_perimeter,
    #                       10, 0)
    @unittest.skipUnless(sys.platform.startswith('win'),
                         'Requires Windows')
    def test_error(self):  ##Cleaner than above##
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10, 0)

if __name__ == '__main__':
    unittest.main()