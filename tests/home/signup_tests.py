from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class SignupTests():

    def test_validSignup(self):
        baseURL = "http://test6nov.gmastesttest.com/"
        driver = webdriver.Chrome(
            executable_path='/home/akt/Downloads/pycharm-community-2019.3.1/bin/driver/chromedriver')
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        signupLink = driver.find_element(By.CSS_SELECTOR, value="#user-register")
        signupLink.click()

        # Signup form data
        firstName = driver.find_element(By.CSS_SELECTOR, value="#id_firstname")
        lastName = driver.find_element(By.CSS_SELECTOR, value="#id_lastname")
        email = driver.find_element(By.CSS_SELECTOR, value="#register_id_email")
        contactNo = driver.find_element(By.CSS_SELECTOR, value="#id_contact")
        password = driver.find_element(By.CSS_SELECTOR, value="#register_id_password")
        confirmPassword = driver.find_element(By.CSS_SELECTOR, value="#id_confirm_password")
        referralLink = driver.find_element(By.LINK_TEXT, "Have a referral code?")
        referralCode = driver.find_element(By.CSS_SELECTOR, value="#id_referrer_code")
        signupButton = driver.find_element(By.CSS_SELECTOR, value="#user-signup-submit")

        firstName.send_keys("referred08")
        lastName.send_keys("Tripathi")
        email.send_keys("referred08@gmail.com")
        contactNo.send_keys("9891320008")
        password.send_keys("test1")
        confirmPassword.send_keys("test1")
        referralLink.click()
        referralCode.send_keys("EISUdh")
        signupButton.click()
        time.sleep(20)


ff = SignupTests()
ff.test_validSignup()