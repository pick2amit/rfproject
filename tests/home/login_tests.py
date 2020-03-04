from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    baseURL = "http://test6nov.gmastesttest.com/"
    driver = webdriver.Chrome(executable_path='/home/akt/Downloads/pycharm-community-2019.3.1/bin/driver/chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(5)
    lp = LoginPage(driver)


    @pytest.mark.tryfirst
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("", "")

        result = self.lp.verifyLoginError()
        assert result == True

    @pytest.mark.trylast
    def test_validLogin(self):
        self.driver.refresh()
        self.lp.login("referred02@gmail.com", "test1")

        result = self.lp.verifyLogoutElement()
        assert result == True
        self.driver.quit()
