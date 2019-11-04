import os
import os.path as path

from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        lib_directory = base_directory + '/libs'
        driver_location = lib_directory + '/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)
        driver.get('http://www.letskodeit.com')


ff = RunFFTests()
ff.testMethod()
