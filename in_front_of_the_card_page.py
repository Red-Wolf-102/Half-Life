from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from base_class import Base

class In_front_of_the_card_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    age_year = "//select[@id='ageYear']"
    age_year_2000 = "//option[@value='2000']"
    view_product_page_btn = "//a[@id='view_product_page_btn']"

    def get_age_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_year)))
    def get_age_year_2000(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_year_2000)))
    def get_view_product_page_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.view_product_page_btn)))

    def click_age_year(self):
        self.get_age_year().click()
        print("Click age_year")
    def click_age_year_2000(self):
        self.get_age_year_2000().click()
        print("Click age_year_2000")
    def click_view_product_page_btn(self):
        self.get_view_product_page_btn().click()
        print("Click view_product_page_btn")

    def age_verification(self):
        # time.sleep(3)
        self.get_current_url()
        # time.sleep(3)
        self.click_age_year()
        # time.sleep(3)
        self.click_age_year_2000()
        # time.sleep(3)
        self.get_screenshot()
        # time.sleep(3)
        self.click_view_product_page_btn()
        # time.sleep(3)