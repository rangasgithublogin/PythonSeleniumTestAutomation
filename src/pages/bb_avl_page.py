from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class BbAvlPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'address': ('ID', "wialus-search-input"),
        'listedAddress': ('CSS', ".selected"),
        'search_icon': ('CSS', ".address-search-icon"),
        'result': (By.XPATH, "//div[@class='location-details-now']/ul/li")
    }

    def select_address(self, txt):
        self.address.set_text(txt)

    def click_search(self):
        self.search_icon.click()

    def click_address(self):
        self.listedAddress.click()

    def get_result(self):
        return self.result.text