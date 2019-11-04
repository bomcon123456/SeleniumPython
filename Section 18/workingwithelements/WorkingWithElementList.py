import os
import os.path as path
import time

from selenium import webdriver


class WorkingWithElementList():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        radioButtonsList = driver.find_elements_by_xpath(
                '//input[contains(@type, \'radio\') and contains(@name,\'cars\')]'
        )
        size = len(radioButtonsList)
        print('Size of list:', size)
        for button in radioButtonsList:
            isSelected = button.is_selected()
            if not isSelected:
                button.click()
                time.sleep(1)


ff = WorkingWithElementList()
ff.test()
