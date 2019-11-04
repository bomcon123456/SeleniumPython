import os
import os.path as path

from selenium import webdriver


class WorkingWithElementList():
    def test(self):
        base_url = 'http://www.expedia.com'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_id('tab-flight-tab-hp').click()
        driver.find_element_by_xpath('//div[@id=\'traveler-selector-hp-flight\']//button').click()
        driver.find_element_by_xpath(
                '/html/body/meso-native-marquee/section/div/div/div[1]'
                '/section/div/div[2]/div[2]/section[1]/form/fieldset[2]'
                '/div/div[4]/div/div/ul/li/div/div/div/div[2]/div[1]/div[4]/button').click()
        element = driver.find_element_by_xpath(
                '/html/body/meso-native-marquee/section/div/div/div[1]/section/div'
                '/div[2]/div[2]/section[1]/form/fieldset[2]/div/div[4]'
                '/div/div/ul/li/div/div/div/div[2]/div[2]')
        print(element.is_displayed())


ff = WorkingWithElementList()
ff.test()
