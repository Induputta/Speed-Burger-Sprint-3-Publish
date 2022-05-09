#Selenium test script
#test script to verify a valid user is logged in successfully
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import warnings


class ll_ATS(unittest.TestCase):
    #set up the test class - assign the driver to Chrome - if using a different
    #browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning) #ignore resource warning if occurs

    # If login is successful, 'Logout' will be displayed as the text in the Navbar
    def test_ll(self):

        #open the browser and go to the admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        elem = driver.find_element(By.XPATH,'//*[@id="subheader"]/span/a').click()
        user = "instructor"  # must be a valid username for the application
        pwd = "maverick2"  # must be the password for a valid user
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        time.sleep(5)  # pause to allow screen to load
        #if the Logout Link Text is found on the screen
        #   assert "Logged in" is True
        try:
           elem = driver.find_element(By.XPATH, '//*[@id="subheader"]/span/a').click()
           time.sleep(3)
           print("Test Passed - Valid user is logged in and out successfully")
           assert True

        #else report that the test failed
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()