from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-index='2'][data-component-id='18']")

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT)
