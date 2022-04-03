import unittest
from Nova88MYRGetBalanceTestCase import Nova88MYRGetBalanceTestCase
from Nova88MYRLoginTestCase import Nova88MYRLoginTestCase
from Nova88MYRTransferTestCase import Nova88MYRTransferTestCase

def suite(testcase):
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    testcases = {Nova88MYRGetBalanceTestCase, Nova88MYRLoginTestCase}
    for testcase in testcases:
        runner.run(suite(testcase))