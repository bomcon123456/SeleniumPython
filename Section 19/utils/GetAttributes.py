import os
import os.path as path

from selenium import webdriver


class GetAttributes():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id('name')
        print('ClassValue', element.get_attribute('class'))
        print('TypeValue', element.get_attribute('type'))

        driver.quit()


ff = GetAttributes()
ff.test()
