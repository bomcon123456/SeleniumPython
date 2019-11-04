import os
import os.path as path

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByDemo():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)
        driver.get(base_url)

        elements = driver.find_elements(By.CLASS_NAME, 'inputs')
        length = len(elements)
        if elements is not None:
            print('Size of the list: ' + str(length))


ff = FindByDemo()
ff.test()
