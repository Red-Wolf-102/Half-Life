from selenium import webdriver
import time
from main_page import Main_page
from search_page import Search_page
from in_front_of_the_card_page import In_front_of_the_card_page
from card_page import Card_page

def test_elden_ring_shadow_of_the_erdtree_deluxe_edition(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    m_p = Main_page(driver)
    m_p.search_in_header()

    # time.sleep(3)

    s_p = Search_page(driver)
    s_p.search_on_search_page()

    # time.sleep(3)

    i_f_o_t_c_p = In_front_of_the_card_page(driver)
    i_f_o_t_c_p.age_verification()

    # time.sleep(3)

    c_p = Card_page(driver)
    c_p.adding_a_card_to_the_cart()

    # time.sleep(3)

    driver.close()
    driver.quit()