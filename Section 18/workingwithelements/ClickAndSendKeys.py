import os
import os.path as path
import time

from selenium import webdriver


class ClickAndSendKeys():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        button = driver.find_element_by_xpath('//div[@id=\'navbar\']//a[@href=\'/sign_in\']')
        button.click()

        username_textbox = driver.find_element_by_id('user_email')
        username_textbox.send_keys('test')
        password_textbox = driver.find_element_by_id('user_password')
        password_textbox.send_keys('test')

        time.sleep(3)
        username_textbox.clear()
        time.sleep(3)
        username_textbox.send_keys('test')


ff = ClickAndSendKeys()
ff.test()
