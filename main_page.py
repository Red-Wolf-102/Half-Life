from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base_class import Base

class Main_page(Base):

    url = "https://store.steampowered.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    store_nav_search_term = "//input[@id='store_nav_search_term']"

    def get_store_nav_search_term(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.store_nav_search_term)))
    def get_store_search_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.store_search_link)))

    def input_store_nav_search_term(self, store_nav_search_term):
        self.get_store_nav_search_term().send_keys(store_nav_search_term)
        print("Input store_nav_search_term")
    def enter_store_nav_search_term(self):
        self.get_store_nav_search_term().send_keys(Keys.ENTER)
        print("Enter store_nav_search_term")

    def search_in_header(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        # time.sleep(3)
        self.get_current_url()
        # time.sleep(3)
        self.input_store_nav_search_term("dark souls")
        # time.sleep(3)
        self.get_screenshot()
        # time.sleep(3)
        self.enter_store_nav_search_term()
        # time.sleep(3)