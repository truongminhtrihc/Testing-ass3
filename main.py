import unittest
import argparse
from func_toan import Test_NewEventWithEquivalence
from changePassword import Module1Test, Module2Test
from newevent import Module2TestBoudary, Module1TestUsecase
from enrol_users import Test_EnrolUser
def suite_func_toan():
    suite = unittest.TestSuite()
    for i in range(1, 48):
        suite.addTest(Test_NewEventWithEquivalence(f'test_{i}'))
    return suite
def suite_enrol_user():
    suite = unittest.TestSuite()
    testlst = [1,2,3,5,6,7,8,9,10,11,12,13,14,15]
    for i in testlst:
        suite.addTest(Test_EnrolUser(f"test_UCT_{i}"))
    return suite
def suite_changePassword():
    suite = unittest.TestSuite()
    test_modules = [Module1Test, Module2Test]
    for module in test_modules:
        suite.addTest(unittest.makeSuite(module))
    return suite

def suite_newevent():
    suite = unittest.TestSuite()
    test_modules = [Module1TestUsecase, Module2TestBoudary]
    for module in test_modules:
        suite.addTest(unittest.makeSuite(module))
    return suite

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific test suite.')
    parser.add_argument('test_suite', choices=['suite_func_toan', 'suite_changePassword', 'suite_newevent'],
                        nargs='?', help='Choose which test suite to run.')
    args = parser.parse_args()

    if args.test_suite == 'suite_func_toan':
        runner = unittest.TextTestRunner()
        runner.run(suite_func_toan())
    elif args.test_suite == 'suite_changePassword':
        runner = unittest.TextTestRunner()
        runner.run(suite_changePassword())
    elif args.test_suite == 'suite_newevent':
        runner = unittest.TextTestRunner()
        runner.run(suite_newevent())
    else:
        parser.print_help()
