from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

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

    def get_result_by_simple_xpath(self):
        return self.result.text

    def get_result_using_explicit_wait(self, txt):
        wdw = WDW(self.driver, 5)
        return wdw.until(EC.visibility_of_element_located((By.XPATH, "//li[text()='{0}']".format(txt)
                                                           ))).is_displayed()

    def get_result_by_lambda(self, txt):
        return len(list(filter(lambda ele: ele.text == txt,
                      self.driver.find_elements(By.XPATH, "//div[@class='location-details-now']//li"))))

