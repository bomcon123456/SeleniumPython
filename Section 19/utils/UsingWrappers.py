import os
import os.path as path

from selenium import webdriver

from .HandyWrappers import HandyWrappers


class UsingWrappers():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        hw = HandyWrappers(driver)
        textField = hw.getElement('name')
        textField.send_keys('Teset')


ff = UsingWrappers()
ff.test()
