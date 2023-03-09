from selenium import webdriver
from src.pages.bb_avl_page import BbAvlPage


def test_check_bb_availability():
    driver = webdriver.Chrome()
    driver.get("https://www.chorus.co.nz/tools-support/broadband-tools/broadband-map")
    bb_page = BbAvlPage(driver)
    bb_page.select_address("19A Woodland Road, Johnsonville, Wellington")
    bb_page.click_address()
    bb_page.click_search()
    assert bb_page.get_result_by_simple_xpath() == "UFB fibre up to 1 Gbps"
    assert bb_page.get_result_using_explicit_wait("Hyperfibre up to 4 Gbps")
    assert bb_page.get_result_by_lambda("Hyperfibre up to 8 Gbps") == 1
    driver.quit()