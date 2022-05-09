# Unit test file to determine if the Home page is displayed when the user logged in
# clicks the 'Check our menu here' button in the home page
# clicks a food item 'All Veggie' in menu list
# clicks the 'Add to cart' button
# A food item got added if All Veggie food item is added to cart and Checkout button exists on new screen
# after clicking "Add to Cart" button
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import warnings


class ll_ATS(unittest.TestCase):

    def is_text_present(self, text):
        return str(text) in self.driver.page_source
    # set up the test class - assign the driver to Chrome - if using a different

    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs
    # Test if Check our menu here  list is displayed when user logged in

    # Test if food item 'All Veggie' is added to the cart 'Add to cart' button is clicked

    # Cart page is shown if the 'All Veggie' food item is added to cart and Checkout button exists on new screen
    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load
        # click the login button - user must be logged in to view the Home page of speed burger
        elem = driver.find_element(By.XPATH,
    '//*[@id="subheader"]/span/a').click()


        # find the username and password input boxes and login
        user = "instructor"  # must be a valid username for the application
        pwd = "maverick2"  # must be the password for a valid user
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to load
        # find 'Check our menu here' and click it – note this is all one Python statement
        elem = driver.find_element(By.XPATH,
    '//*[@id="content"]/div[1]/div[2]/div/a').click()
        time.sleep(3)  # pause to allow screen to change

        # find 'All Veggie' Food Item and click it – note this is all one Python statement
        elem = driver.find_element(By.XPATH,
    '//*[@id="main"]/div[1]/a[2]').click()
        time.sleep(3)  # pause to allow screen to change

        # find 'Add to Cart' button and click it
        elem = driver.find_element(By.XPATH,
    '//*[@id="content"]/div/form/input[3]').click()
        time.sleep(3)  # pause to allow screen to change


        try:
            # verify All Veggie food item is added to cart after clicking "Add to Cart" button
            self.is_text_present("All Veggie")
            # verify Checkout button exists on new screen after clicking "Add to Cart" button
            elem = driver.find_element(By.XPATH,
                    '//*[@id="content"]/p/a[2]')
            print("Test passed - Item is added to cart")
            assert True
        except NoSuchElementException:
            self.fail("Item List does not appear when 'Add to Cart' is clicked - test failed")
def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()