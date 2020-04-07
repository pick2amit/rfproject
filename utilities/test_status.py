from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import utilities.capture_screenshot as screen

import logging

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)


    def __init__(self, driver):
        """
        Inits checkpoint class
        :param driver:
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("####  VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("####  VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)


            else:
                self.resultList.append("FAIL")
                self.log.error("####  VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("#######  Exception Occurred :: + " + resultMessage)
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):
        """
        Mark the result of verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the Final result of verification point in a test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ####  TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.error(testName + " #### TEST SUCCESS")
            self.resultList.clear()
            assert True == True
