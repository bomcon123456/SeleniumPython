import os
import os.path as path

from selenium import webdriver


class BrowserInteractions():
    def test(self):
        base_url = 'https://learn.letskodeit.com/p/practice'
        base_directory = path.abspath(path.join(os.getcwd(), "../.."))
        driver_location = base_directory + '/libs/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_location)

        # Maximize window
        driver.maximize_window()
        # Open URL
        driver.get(base_url)
        # Get title
        print('Title:', driver.title)
        # Get current url
        print('Current url:', driver.current_url)
        # Refresh
        driver.refresh()
        # 2nd method:
        driver.get(driver.current_url)
        # Open another
        driver.get('https://google.com')
        # Browser back, forward
        driver.back()
        driver.forward()
        # Get Page source
        print('Page Source:', driver.page_source)
        # Close
        driver.close()
        # Quit
        # driver.quit()


ff = BrowserInteractions()
ff.test()
