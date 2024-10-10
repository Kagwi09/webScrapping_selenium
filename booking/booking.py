import booking.constants as const
from selenium import webdriver
import os


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\Users\MWANGI\Documents\Python Scripts\selenium\chromedriver-win64",
                 tear_down=False):
        self.chrome_driver_path = driver_path
        self.teardown = tear_down
        os.environ['PATH'] += r"C:\Users\MWANGI\Documents\Python Scripts\selenium\chromedriver-win64"
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        # exit function

    def land_first_page(self):
        self.get(const.BASE_URL)
