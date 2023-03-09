from selenium import webdriver
from src.pages.bb_avl_page import BbAvlPage


def test_check_bb_availability():
    driver = webdriver.Chrome()
    driver.get("https://www.chorus.co.nz/tools-support/broadband-tools/broadband-map")
    bb_page = BbAvlPage(driver)
    bb_page.select_address("19A Woodland Road, Johnsonville, Wellington")
    bb_page.click_address()
    bb_page.click_search()
    assert bb_page.get_result() == "UFB fibre up to 1 Gbps"
    driver.quit()