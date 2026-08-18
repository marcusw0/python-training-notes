import unittest

class TestMultiplication(unittest.TestCase):
    def runTest(self):
        self.assertEqual((3 * 5), 12)

class TestAddition(unittest.TestCase):
    def runTest(self):
        self.assertEqual((1 + 5), 6)

class TestDivision(unittest.TestCase):
    def runTest(self):
        self.assertEqual((7 / 0), 1)

class SimpleTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)

    @unittest.skip('Temporarily skips test')
    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(TestMultiplication())
    # suite.addTests([TestAddition(), TestDivision()])
    suite = unittest.makeSuite(SimpleTest, 'test')
    suite.addTests([TestAddition(), TestDivision(), TestMultiplication()])
    results = unittest.TextTestRunner(verbosity=2).run(suite)

    print('Errors: ', results.errors)
    print('\nFailures: ', results.failures)
    print('\nSkipped Tests: ', results.skipped)
    print('\nNo. of Tests: ', results.testsRun)
    print('\nWas it a successful test? ', results.wasSuccessful())