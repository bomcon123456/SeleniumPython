import os
import os.path as path

from selenium import webdriver


class ElementState():
    def test(self):
        base_url = 'https://www.google.com'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_xpath('//div[@class=\'a4bIc\']//input[@class=\'gLFyf gsfi\']')
        if element.is_enabled():
            element.send_keys('abc')


ff = ElementState()
ff.test()
