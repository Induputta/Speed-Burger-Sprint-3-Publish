# Unit test file to determine if the Home page is displayed when the user logged in
# clicks the 'Check our menu here' button in the home page
# clicks a food item 'All Veggie' in menu list
# clicks the 'Add to cart' button
# Test the Checkout option by filling the user and card details
# Payment is done if 'Your payment was successful' is shown on the new screen
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
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

    # Test if 'Checkout' button is clicked

    # Test the Checkout option by filling the user and card details

    # Payment is done if 'Your payment was successful' is shown on the new screen
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

        # find 'Checkout' button and click it
        elem = driver.find_element(By.XPATH,
    '//*[@id="content"]/p/a[2]').click()
        time.sleep(3)  # pause to allow screen to change

        first_name = "Indu"
        last_name = "Putta"
        email = "iputta@unomaha.edu"
        address = "6001 Dodge St,NE"
        postal_code = "68182"
        city = "Omaha"

        elem = driver.find_element(By.ID, "id_first_name")
        elem.send_keys(first_name)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element(By.ID, "id_last_name")
        elem.send_keys(last_name)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element(By.ID, "id_email")
        elem.send_keys(email)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element(By.ID, "id_address")
        elem.send_keys(address)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element(By.ID, "id_postal_code")
        elem.send_keys(postal_code)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element(By.ID, "id_city")
        elem.send_keys(city)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to change

        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-number']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='credit-card-number']"))).send_keys("4111111111111111")
        driver.switch_to.default_content()

        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cvv']"))).send_keys("100")
        driver.switch_to.default_content()

        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-expirationDate']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='expiration']"))).send_keys("05/2024")
        driver.switch_to.default_content()
        time.sleep(3)  # pause to allow screen to change

        # find 'Pay' button and click it
        elem = driver.find_element(By.XPATH,
    '//*[@id="payment"]/input[3]').click()

        try:
            # verify the text 'Your payment was successful' after clicking "Pay" button
            self.is_text_present("Your payment was successful")
            print("Test passed - Item is added to cart")
            assert True
        except NoSuchElementException:
            self.fail("Payment is successfull is not displayed when 'Pay' button is clicked - test failed")
def tearDown(self):
    self.driver.close()
if __name__ == "__main__":
    unittest.main()