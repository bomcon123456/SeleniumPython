from traceback import print_stack

from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .HandyWrappers import HandyWrappers


class ExplicitWaitType:
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        byType = self.hw.getByType(locatorType)
        try:
            print('Waiting for maximum :: ' + str(timeout), ':: seconds for the element to be clickable')
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print('Element appeared on the web page')
        except:
            print('Element not appeared')
            print_stack()
        return element
