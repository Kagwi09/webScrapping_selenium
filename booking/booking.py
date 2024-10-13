import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


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
        close_button = self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]')
        close_button.click()

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


