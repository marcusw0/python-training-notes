import unittest
import triangle_area

class TestArea(unittest.TestCase):

    # def triangle_test(self):  ##has to start with test_##
        # results = triangle_area.triangle(10, 5)
        # self.assertEqual(results, 25)

    # def test_triangle(self):  ##This runs successfully
    #     results = triangle_area.triangle(10, 5)
    #     self.assertEqual(results, 25)

    def runTest(self):  #This has the same output as test_triangle
        results = triangle_area.triangle(10, 5)
        self.assertEqual(results, 25)

if __name__ == '__main__':
    unittest.main()