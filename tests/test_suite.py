import unittest
from tests.home.login_tests import LoginTests
#from tests.home.signup_tests import SignupTests

# Get all tests from the test class
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTests)

# Create a test suite combining all test cases
smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner().run(smokeTest)
