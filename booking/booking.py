
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\Users\MWANGI\Documents\Python Scripts\selenium\chromedriver-win64",
                 tear_down=False):
        self.chrome_driver_path = driver_path
        self.teardown = tear_down
        os.environ['PATH'] += r"C:\Users\MWANGI\Documents\Python Scripts\selenium\chromedriver-win64"
        super(Booking, self).__init__()

        # add an implicit wait clause
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        # exit function

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        # Wait up to 10 seconds for the close button to be present
        try:
            close_button = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'))
            )
            close_button.click()
        except TimeoutException:
            print("Popup did not appear, skipping the close_popup method.")

    def change_currency(self, currency=None):
        # Find and click the currency picker button
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="footer-currency-picker-trigger-desktop"]'
        )
        currency_element.click()

        # Use the *= operator to match the div that contains the class "CurrencyPicker_currency"
        currency_selector = f'div[class*="CurrencyPicker_currency"]'

        # Find all currency elements matching the selector
        currency_elements = self.find_elements(By.CSS_SELECTOR, currency_selector)

        # Iterate over the currency elements and click the one matching the specified currency (e.g., 'USD')
        for element in currency_elements:
            if currency in element.text:
                element.click()  # Click the element that contains the specified currency
                break

    def select_destination(self, destination):
        try:
            # Locate the search field by class name
            search_field = self.find_element(By.CLASS_NAME, 'eb46370fe1')

            # Clear the search field and enter the destination
            search_field.clear()
            search_field.send_keys(destination)

            # Adding a delay to allow suggestions to load
            time.sleep(2)

            # Wait for the first result to be visible, then click it
            first_result = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#autocomplete-result-0 div[role="button"]'))
            )
            print(first_result.text)

            first_result.click()
        except TimeoutException:
            print("No search results appeared, or the first result could not be found.")


