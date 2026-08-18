import unittest
import shape_area

class TestArea(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(shape_area.triangle(10, 5), 25)

    def test_rectangle(self):
        # self.assertEqual(shape_area.rectangle(6, 7), 26) #AssertionError: 42 != 26
        self.assertEqual(shape_area.rectangle(6, 7), 42)

    def test_square(self):
        self.assertEqual(shape_area.square(7), 49)

if __name__ == '__main__':
    unittest.main()


#######################################################
#  Different ways to run test script:
#    $ python3 \
#    > -m unittest test_shape_area.py
#    ...
#    ----------------------------------------------------------------------
#    Ran 3 tests in 0.000s
#    
#    OK

#    $ python3 -m unittest \
#    > -q test_shape_area.TestArea.test_square -v
#    test_square (test_shape_area.TestArea) ... ok
#    
#    ----------------------------------------------------------------------
#    Ran 1 test in 0.000s
#    
#    OK

#    $ python3 -m unittest \
#    > -q test_shape_area.TestArea.test_square \
#    > test_shape_area.TestArea.test_rectangle -v
#    test_square (test_shape_area.TestArea) ... ok
#    test_rectangle (test_shape_area.TestArea) ... ok
#    
#    ----------------------------------------------------------------------
#    Ran 2 tests in 0.000s
#    
#    OK

###  -m specifies the module and -q specifies quiet mode to reduce console output