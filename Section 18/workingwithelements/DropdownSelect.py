import os
import os.path as path
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class WorkingWithElementList():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id('carselect')
        select = Select(element)

        select.select_by_value('benz')
        time.sleep(1)
        select.select_by_index('2')
        time.sleep(1)
        select.select_by_visible_text('BMW')
        time.sleep(1)
        select.select_by_index(2)
        time.sleep(1)


ff = WorkingWithElementList()
ff.test()
