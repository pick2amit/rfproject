import time
import os

def screenShot2(self, resultMessage):
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
