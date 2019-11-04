from selenium.webdriver.common.by import By


class HandyWrappers:
    def __init__(self, driver):
        self.driver = driver

    def getByType(selfself, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        print('Not supported.')
        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        byType = self.getByType(locatorType)
        try:
            element = self.driver.find_element(byType, locator)
        except:
            print('Not found.')
        return element

    def isElementPresent(self, locator, byType):
        element = self.getElement(locator, byType)
        return element is not None

    def elementPresenceCheck(self, locator, byType):
        elementList = None
        try:
            elementList = self.driver.find_elements(byType, locator)
        except:
            return False
        if len(elementList) > 0:
            return True
        return False
