from traceback import print_stack
from selenium.common.exceptions import *
import os
import time
import utilities.custom_logger as cl
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        self.log.info("$$$$$$$$$$$$ sc directory is: " + screenshotDirectory)
        relativeFileName = screenshotDirectory + fileName
        self.log.info("$$$$$$$$$$$$ relative File: " + relativeFileName)
        currentDirectory = os.path.dirname(__file__)
        self.log.info("$$$$$$$$$$$$ current dir: " + currentDirectory)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        self.log.info("$$$$$$$$$$$$ destination File: " + destinationFile)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        self.log.info("$$$$$$$$$$$$ destination dir: " + destinationDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshots saved to directory " + destinationFile)
        except:
            self.log.error("###### Exception Occurred")



    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Script FAIL: " + "Locator Type " + locatorType + " not correct supported")

            return False

    def getTitle(self):
        self.log.info("Page Title is: " + self.driver.title)
        return self.driver.title

    def getElement(self, locator, locatorType="xpath", element=None):
        element = None
        try:
            time.sleep(2)
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)

            self.log.info("Element FOUND with locator: " + locator + ", locatorType: " + locatorType)
        except:
            self.log.info("Script FAIL: " + "Element NOT FOUND with locator: " + locator + ", locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="xpath"):
        try:
            time.sleep(2)
            element = self.getElement(locator, locatorType)
            element.click()

            self.log.info("Element Clicked with locator: " + locator + ", locatorType: " + locatorType)
        except:
            self.log.info("Script FAIL: " + "Element not CLICKED with locator: " + locator + ", locatorType: " + locatorType)
            #print_stack()

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            time.sleep(2)
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on Element with locator: " + locator + ", locatorType: " + locatorType)
        except:
            self.log.info("Script FAIL: " + "Data not SENT to Element with locator: " + locator + ", locatorType: " + locatorType)
            #print_stack()

    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element FOUND with locator: " + locator + ", locatorType: " + locatorType)
                return True
            else:
                self.log.info("Script FAIL: " + "Element NOT FOUND with locator: " + locator + ", locatorType: " + locatorType)
                return False
        except:
            self.log.info("Script FAIL: " + "Element NOT FOUND with locator: " + locator + ", locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element/Elements found with locator: " + locator + ", locatorType: " + byType)
                return True
            else:
                self.log.info("Script FAIL: " + "Element/Elements not FOUND with locator: " + locator + ", locatorType: " + byType)
                return False
        except:
            self.log.info("Script FAIL: " + "Element/Elements not FOUND with locator: " + locator + ", locatorType: " + byType)
            return False
    """
    def waitForElement(self, locator, locatorType="css", timeout=10, pollFrequency=1.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for elements to be clickable")
            wait = WebDriverWait(self.driver, timeout, pollFrequency,
                                 ignored_exception = [NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType, "stopFilter_stops-0"))
            print("element appeared on the webpage")

        except:
            print("element not appeared on the webpage")
            print_stack()
        return element
    """