import unittest
from test_search import PythonOrgSearch
from test_abc import PythonOrgSearchABC
from func_toan import Test_NewEventWithEquivalence
from enrol_users import Test_EnrolUser
from func2 import Module1Test,Module2Test
from func1 import Module2TestBoudary,Module1TestUsecase
def suite_func_toan():
    suite = unittest.TestSuite()
    ## add tung test cu the -> prevent random testcase in your class :))
    for i in range(1, 48):
        suite.addTest(Test_NewEventWithEquivalence(f'test_{i}'))
    return suite
def suite_enrol_user():
    suite = unittest.TestSuite()
    testlst = [1,2,3,5,6,7,8,9,10,11,12,13,14,15]
    for i in testlst:
        suite.addTest(Test_EnrolUser(f"test_UCT_{i}"))
    return suite
def suite_func2():
    suite = unittest.TestSuite()
    test_modules = [Module1Test, Module2Test]
    for module in test_modules:
        suite.addTest(unittest.makeSuite(module))
    return suite
def suite_func1():
    suite = unittest.TestSuite()
    test_modules = [Module1TestUsecase,Module2TestBoudary]
    for module in test_modules:
        suite.addTest(unittest.makeSuite(module))
    return suite

if __name__ == "__main__":
    # Create runner
    runner = unittest.TextTestRunner()
    runner.run(suite_enrol_user())
    runner.run(suite_func1())
    # runner.run(suite_func_toan())
