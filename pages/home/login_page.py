from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    _login_link = "//a[@class='js-login-trigger']"
    _login_email = "//input[@id='id_login_username']"
    _login_password = "//input[@id='id_login_password']"
    _login_button = "//input[@id='submit']"

    _overlay_popup_id = "overlayPopup"
    _cross_icon = "//div[@class='subscription-popup-background soft-double--bottom']//div//i[@class='micon micon-cross-white']"

    _profile_menu = "//a[contains(@class,'show-for-medium-up push-half--left')]"
    _logout_link = "//a[text()='Log Out']"

    # By defaults we use locatorType="xpath", specify it if u use any other

    def click_login_link(self):
        self.elementClick(self._login_link)

    def enter_email(self, email):
        self.sendKeys(email, self._login_email)

    def enter_password(self, password):
        self.sendKeys(password, self._login_password)

    def click_loginbtn(self):
        self.elementClick(self._login_button)

    def click_profileMenu(self):
        self.elementClick(self._profile_menu)

    def click_logout(self):
        self.elementClick(self._logout_link)


    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_loginbtn()
        time.sleep(3)

    def logout(self):
        self.click_profileMenu()
        self.click_logout()

    def verify_login_success(self):
        # If logout link is present that means user login successfully
        return self.isElementPresent(self._logout_link)

    def verify_login_fail(self):
        # If error message found then we can say login fails
        return self.isElementPresent(self._login_error)

    def verify_Login_title(self):
        return self.verifyPageTitle("dashboard")
