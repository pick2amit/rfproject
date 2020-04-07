from base.selenium_driver import SeleniumDriver
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
                    Inits checkpoint class
                    :param driver:
                    """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, expectedTitle):
        """
        Verify the page title

        :param expectedTitle: Page title that needs to be verified
        :return: True or False
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, expectedTitle)
        except:
            self.log.error("Failed to get the page title")
            return False

