import os
import os.path as path

from selenium import webdriver


class FindByClassNameTagName():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)
        driver.get(base_url)

        element = driver.find_element_by_class_name('displayed-class')
        if element is not None:
            print('We found an element')

        element2 = driver.find_element_by_tag_name('a')
        if element2 is not None:
            print('We found another element')


ff = FindByClassNameTagName()
ff.test()
