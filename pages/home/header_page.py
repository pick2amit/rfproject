from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time
import utilities.custom_logger as cl
import logging

class HeaderPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    _login_link = "//*[@id='enduser_auth_wrap']//a[@id='user-login']"
    _login_email = "//input[@id='login_id_email']"
    _login_password = "//input[@id='login_id_password']"
    _login_button = "//button[@class='theme-btn theme-btn-solid login-btn']"


    _login_error = "//label[@id='login_id_email-error']"
    _about_link = "//a[@class='primary-link'][contains(text(),'About')]"

    _store_logo = "//div[@id='logo']//div[@id='logo']"
    _track_order = "//a[@id='track_order']"
    _user_menu = "//li[@class='dropdown']//a[@id='enduser_accounts']"

    _profile = "//li[@class='dropdown open']//strong[contains(text(),'Profile')]"
    _my_order = "//a[@class='secondary-link'][contains(text(),'My orders')]"
    _my_address = "//a[@class='secondary-link'][contains(text(),'My Address')]"
    _wishlist = "//a[@class='secondary-link'][contains(text(),'My Wish List')]"
    _change_pwd = "//a[@class='secondary-link'][contains(text(),'Change Password')]"
    _logout_link = "//a[@class='secondary-link'][contains(text(),'Logout')]"

    # By defaults we use locatorType="xpath", specify it if u use any other
    def click_user_menu(self):
        self.elementClick(self._user_menu)

    def click_logout(self):
        self.elementClick(self._logout_link)