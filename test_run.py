import unittest
from SignUpTestCase import SignUpTestCase
from SignInTestCase import SignInTestCase

def suite(testcase):
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    testcases = {SignUpTestCase, SignInTestCase}
    for testcase in testcases:
        runner.run(suite(testcase))