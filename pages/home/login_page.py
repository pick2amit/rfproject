from selenium.webdriver.common.by import By
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    # Locators
    _login_link = "Login"
    _login_email = "#login_id_email"
    _login_password = "#login_id_password"
    _login_button = "//button[@class='theme-btn theme-btn-solid login-btn']"

    _logout_link = "//a[@class='secondary-link'][contains(text(),'Logout')]"
    _login_error = "#login_id_password-error"

    # //button[@class='theme-btn theme-btn-solid login-btn'] OR //div/form/button

    # methods for individual WebElement
    def getLoginLink(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, self._login_link)

    def getLoginEmail(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_email)

    def getLoginPassword(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_password)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def getLogoutLink(self):
        return self.driver.find_element(By.XPATH, self._logout_link)

    def getLoginError(self):
        return  self.driver.find_element(By.CSS_SELECTOR, self._login_error)

    # Creating respective/action for the webelements
    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getLoginEmail().send_keys(email)

    def enterPassword(self, password):
        self.getLoginPassword().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def verifyLogoutElement(self):
        rr = self.getLogoutLink()
        if rr is not None:
            return True
        else:
            return False

    def verifyLoginError(self):
        result = self.getLoginError()
        if result is not None:
            return  True
        else:
            return False

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)

    def verifyLoginSuccess(self):
        self.verifyLogoutElement()

    def verifyLoginFail(self):
        self.verifyLoginError()
