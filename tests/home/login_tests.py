from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):


    @pytest.yield_fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.tryfirst
    def test_invalidLogin(self):
        self.lp.login(email="", password="")

        result1 = self.lp.verify_Login_title()
        self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verify_login_fail()
        self.ts.markFinal("test invalid login", result2, "Invalid login fails")

    @pytest.mark.trylast
    def test_validLogin(self):
        self.lp.login("referred02@gmail.com", "test1")

        result1 = self.lp.verify_Login_title()
        self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verify_login_success()
        self.ts.markFinal("test valid login", result2, "Login successfully")
