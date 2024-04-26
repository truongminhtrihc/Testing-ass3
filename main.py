import unittest
from test_search import PythonOrgSearch
from test_abc import PythonOrgSearchABC
from func_toan import Test_NewEventWithEquivalence
def suite_func_toan():
    suite = unittest.TestSuite()
    ## add tung test cu the -> prevent random testcase in your class :))
    for i in range(1, 48):
        suite.addTest(Test_NewEventWithEquivalence(f'test_{i}'))
    return suite
def suite_test_search():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PythonOrgSearch))
    return suite
def suite_test_abc():
    suite = unittest.TestSuite()
    ## add nguyen class
    suite.addTest(unittest.makeSuite(PythonOrgSearchABC))
    return suite
if __name__ == "__main__":
    # Create runner
    runner = unittest.TextTestRunner()
    
    runner.run(suite_func_toan())
    runner.run(suite_test_search())
    runner.run(suite_test_abc())