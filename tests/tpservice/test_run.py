import unittest
from Nova88MYRGetBalanceTestCase import Nova88MYRGetBalanceTestCase

def suite(testcase):
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    testcases = {Nova88MYRGetBalanceTestCase}
    for testcase in testcases:
        runner.run(suite(testcase))