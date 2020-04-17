# CHROME_DRIVER_PATH_LOCAL = os.path.join(os.path.dirname(__file__), 'driver/chromedriver.exe')
import unittest
import os
import time
from selenium import webdriver

CHROME_DRIVER_PATH_LOCAL = os.path.join(os.path.dirname(__file__), 'driver/chromedriver')


class SampleScript(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH_LOCAL)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")

    def test_sample_test(self):
        self.driver.find_element_by_name("q").send_keys("Selenium Automation")
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@aria-label = 'Google Search']").click()

    def tearDown(self):
        self.driver.quit()