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

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//*[@id="subheader"]/span/a').click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH,'/html/body/footer/div/div/div[1]/p/a').click()
        time.sleep(1)
        newuser = "newuser9"
        newpw = "newpw@1235"
        elem = driver.find_element(By.XPATH,'//*[@id="id_username"]')
        elem.send_keys(newuser)
        time.sleep(1)
        elem = driver.find_element(By.XPATH,'//*[@id="id_password1"]')
        elem.send_keys(newpw)
        time.sleep(1)
        elem = driver.find_element(By.XPATH,'//*[@id="id_password2"]')
        elem.send_keys(newpw)
        time.sleep(1)
        elem = driver.find_element(By.XPATH,'/html/body/div/form/button').click()
        time.sleep(2)
        #elem = driver.find_element(By.XPATH, '//*[@id="subheader"]/span/a').click()
        #time.sleep(1)

        try:
           elem = driver.find_element(By.XPATH, '//*[@id="id_username"]')
           elem.send_keys(newuser)
           time.sleep(1)
           elem = driver.find_element(By.XPATH,'//*[@id="id_password"]')
           time.sleep(1)
           elem.send_keys(newpw)
           time.sleep(1)
           elem = driver.find_element(By.XPATH,'/html/body/div/form/button').click()
           time.sleep(3)
           print("Test Passed - Valid user is logged in successfully")
           assert True

        #else report that the test failed
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()