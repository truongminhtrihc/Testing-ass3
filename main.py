import unittest
from test_search import PythonOrgSearch
from test_abc import PythonOrgSearchABC

if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestSuite()

    # Add test cases from different files to the suite
    suite.addTest(unittest.makeSuite(PythonOrgSearch))
    suite.addTest(unittest.makeSuite(PythonOrgSearchABC))
    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)
