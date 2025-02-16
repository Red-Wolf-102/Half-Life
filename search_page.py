from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from base_class import Base

class Search_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_filter_control_row = "//div[@data-loc='Похожа на Dark Souls']"
    tab_filter_control_row_2 = "//div[@data-loc='Тёмное фэнтези']"
    tab_filter_control_row_3 = "//div[@data-loc='Сложная']"
    tab_filter_control_row_4 = "//div[@data-loc='Полностью совместима']"
    tab_filter_control_row_5 = "//div[@data-loc='Windows']"
    elden_ring = "//a[@data-ds-appid='1245620']"

    def get_tab_filter_control_row(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_filter_control_row)))
    def get_tab_filter_control_row_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_filter_control_row_2)))   
    def get_tab_filter_control_row_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_filter_control_row_3)))
    def get_tab_filter_control_row_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_filter_control_row_4)))
    def get_tab_filter_control_row_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tab_filter_control_row_5)))
    def get_elden_ring(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.elden_ring)))

    def click_tab_filter_control_row(self):
        self.get_tab_filter_control_row().click()
        print("Click tab_filter_control_row")
    def click_tab_filter_control_row_2(self):
        self.get_tab_filter_control_row_2().click()
        print("Click tab_filter_control_row_2")
    def click_tab_filter_control_row_3(self):
        self.get_tab_filter_control_row_3().click()
        print("Click tab_filter_control_row_3")
    def click_tab_filter_control_row_4(self):
        self.get_tab_filter_control_row_4().click()
        print("Click tab_filter_control_row_4")
    def click_tab_filter_control_row_5(self):
        self.get_tab_filter_control_row_5().click()
        print("Click tab_filter_control_row_5")
    def click_elden_ring(self):
        self.get_elden_ring().click()
        print("Click elden_ring")

    def search_on_search_page(self):
        # time.sleep(3)
        self.get_current_url()
        # time.sleep(3)
        self.click_tab_filter_control_row()
        # time.sleep(3)
        self.click_tab_filter_control_row_2()
        # time.sleep(3)
        self.click_tab_filter_control_row_3()
        # time.sleep(3)
        self.click_tab_filter_control_row_4()
        # time.sleep(3)
        self.click_tab_filter_control_row_5()
        # time.sleep(3)
        self.get_screenshot()
        # time.sleep(3)
        self.click_elden_ring()
        # time.sleep(3)