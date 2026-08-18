import unittest

class Testing(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('beta'.upper(), 'BETA')

    def test_boolean(self):
        x = True
        y = False
        self.assertEqual(x, y)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('Beta'.isupper())

if __name__ == '__main__':
    unittest.main()


#running <<python3 three_testcases_v2.py -v>> returns the testing order:
# test_boolean (__main__.Testing) ... FAIL
# test_isupper (__main__.Testing) ... ok
# test_upper (__main__.Testing) ... ok

# ======================================================================
# FAIL: test_boolean (__main__.Testing)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/mwhite84/.vscode-server/Training/Python/percipio/3-journeyman/pythontesting/unittest/three_testcases_v2.py", line 11, in test_boolean
#     self.assertEqual(x, y)
# AssertionError: True != False

# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
