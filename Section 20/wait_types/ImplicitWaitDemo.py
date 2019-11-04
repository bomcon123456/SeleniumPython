import os
import os.path as path

from selenium import webdriver


class ImplicitWaitDemo():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        login_button = driver.find_element_by_xpath('//div[@id=\'navbar\']//a[@href=\'/sign_in\']')
        login_button.click()

        email_field = driver.find_element_by_id('user_email')
        email_field.send_keys('test')


ff = ImplicitWaitDemo()
ff.test()
