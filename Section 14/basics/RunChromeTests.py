import os
import os.path as path

from selenium import webdriver


class RunChromeTests():
    def testMethod(self):
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        lib_directory = base_directory + '/libs'
        driver_location = lib_directory + '/chromedriver'
        os.environ['webdriver.chrome.driver'] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get('http://www.letskodeit.com')


ff = RunChromeTests()
ff.testMethod()
