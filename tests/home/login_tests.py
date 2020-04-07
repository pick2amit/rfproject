from selenium import webdriver
from pages.home.login_page import LoginPage
from pages.home.header_page import HeaderPage
from utilities.test_status import TestStatus
from utilities.read_data import getCSVData
import unittest
import pytest
import time
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class LoginTests(unittest.TestCase):


    @pytest.yield_fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.header = HeaderPage(self.driver)


    @pytest.mark.tryfirst
    def test_invalidLogin(self):
        self.lp.login(email="", password="")

        result1 = self.lp.verify_Login_title()
        self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verify_login_fail()
        self.ts.markFinal("test invalid login", result2, "Invalid login fails")


    @pytest.mark.trylast
    @data(*getCSVData("/home/akt/PycharmProjects/letsautomate/testdata.csv"))
    @unpack
    def test_validLogin(self, email, password):
        self.lp.login(email, password)

        result1 = self.lp.verify_Login_title()
        self.ts.mark(result1, "Title is incorrect")

        result2 = self.lp.verify_login_success()

        time.sleep(1)
        self.header.click_user_menu()
        time.sleep(1)
        self.header.click_logout()
        time.sleep(5)
        self.ts.markFinal("test valid login", result2, "Login successfully")
