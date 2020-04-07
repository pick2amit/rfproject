import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        :param sec:
        :param info:
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verifyTextContains(self, actualText, expectedText):
        """

        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text from Web UI --> :: " + actualText)
        self.log.info("Expected text from Web --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS  !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS  !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """

        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text from Web UI --> :: " + actualText)
        self.log.info("Expected text from Web --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION MATCHED  !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED  !!!")
            return False

    def verifyListMatch(self, actualList, expectedList):
        """

        :param actualList:
        :param expectedList:
        :return:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, actualList, expectedList):
        """

        :param actualList:
        :param expectedList:
        :return:
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
            else:
                return True

    def getAlphanumeric(self, length, type="letter"):
        """

        :param length:
        :param type:
        :return:
        """
        alphaNum = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alphaNum.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphanumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """

        :param listSize:
        :param itemLength:
        :return:
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList
