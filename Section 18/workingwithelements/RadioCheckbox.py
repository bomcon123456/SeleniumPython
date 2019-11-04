import os
import os.path as path
import time

from selenium import webdriver


class RadioCheckbox():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        bmw_button = driver.find_element_by_id('bmwradio')
        bmw_button.click()

        time.sleep(2)
        benz_button = driver.find_element_by_id('benzradio')
        benz_button.click()

        time.sleep(2)
        bmw_checkbox = driver.find_element_by_id('bmwcheck')
        bmw_checkbox.click()

        time.sleep(2)
        benz_checkbox = driver.find_element_by_id('benzcheck')
        benz_checkbox.click()

        print('BWM Radio selected (T/F): ', str(bmw_button.is_selected()))
        print('Benz Radio selected (T/F): ', str(benz_button.is_selected()))
        print('Benz Checkbox selected (T/F): ', str(benz_checkbox.is_selected()))
        print('BMW Checkbox selected (T/F): ', str(bmw_checkbox.is_selected()))


ff = RadioCheckbox()
ff.test()
