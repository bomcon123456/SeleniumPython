import os
import os.path as path

from selenium import webdriver


class RunSafariTests():
    def testMethod(self):
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        lib_directory = base_directory + '/libs'
        driver_location = lib_directory + '/selenium-server-standalone.jar'
        os.environ['SELENIUM_SERVER_JAR'] = driver_location
        driver = webdriver.Safari()
        driver.get('http://www.letskodeit.com')


ff = RunSafariTests()
ff.testMethod()
