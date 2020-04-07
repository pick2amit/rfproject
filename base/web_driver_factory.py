from  selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser, osType):
        self.browser = browser
        self.osType = osType

    def getWebDriverInstance(self):
        baseURL = "http://test6nov.gmastesttest.com/"

        if self.browser.lower() == "chrome":
            driver = webdriver.Chrome(
                executable_path='/home/akt/Downloads/pycharm-community-2019.3.1/bin/driver/chromedriver')
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)
        return driver
