from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from base_class import Base

class Card_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    btn_add_to_cart = "//a[@id='btn_add_to_cart_1010506']"
    primary_focusable = "//button[@class='DialogButton _DialogLayout Primary Focusable']"
    elden_ring_shadow_of_the_erdtree_deluxe_edition = "//div[@class='EflKs0JjldhDSxbUBaiOp']"

    def get_btn_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_add_to_cart)))
    def get_primary_focusable(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.primary_focusable)))
    def get_elden_ring_shadow_of_the_erdtree_deluxe_edition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.elden_ring_shadow_of_the_erdtree_deluxe_edition)))

    def click_btn_add_to_cart(self):
        self.get_btn_add_to_cart().click()
        print("Click btn_add_to_cart")
    def click_primary_focusable(self):
        self.get_primary_focusable().click()
        print("Click primary_focusable")
    def text_elden_ring_shadow_of_the_erdtree_deluxe_edition(self):
        self.get_elden_ring_shadow_of_the_erdtree_deluxe_edition().click()
        print("Text elden_ring_shadow_of_the_erdtree_deluxe_edition")

    def adding_a_card_to_the_cart(self):
        # time.sleep(3)
        self.get_current_url()
        # time.sleep(3)
        self.click_btn_add_to_cart()
        # time.sleep(3)
        self.get_screenshot()
        # time.sleep(3)
        self.click_primary_focusable()
        # time.sleep(3)
        self.assert_url("https://store.steampowered.com/cart")
        # time.sleep(3)
        self.assert_word(self.get_elden_ring_shadow_of_the_erdtree_deluxe_edition(), "ELDEN RING Shadow of the Erdtree Deluxe Edition")
        time.sleep(3)
        self.get_screenshot()
        # time.sleep(3)