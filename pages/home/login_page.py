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
    _login_link = "//*[@id='enduser_auth_wrap']//a[@id='user-login']"
    _login_link2 = "//div[@class='enduser-login text-right ng-scope']//a[@id='user-login']"
    _login_email = "//input[@id='login_id_email']"
    _login_password = "//input[@id='login_id_password']"
    _login_button = "//button[@class='theme-btn theme-btn-solid login-btn']"

    _logout_link = "//a[@class='secondary-link'][contains(text(),'Logout')]"
    _login_error = "//label[@id='login_id_email-error']"
    _about_link = "//a[@class='primary-link'][contains(text(),'About')]"

    # By defaults we use locatorType="xpath", specify it if u use any other

    def click_login_link(self):
        self.elementClick(self._login_link)

    def enter_email(self, email):
        self.sendKeys(email, self._login_email)

    def enter_password(self, password):
        self.sendKeys(password, self._login_password)

    def click_loginbtn(self):
        self.elementClick(self._login_button)


    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_loginbtn()
        time.sleep(3)

    def verify_login_success(self):
        # If logout link is present that means user login successfully
        return self.isElementPresent(self._logout_link)

    def verify_login_fail(self):
        # If error message found then we can say login fails
        return self.isElementPresent(self._login_error)

    def verify_Login_title(self):
        return self.verifyPageTitle("test6november")
