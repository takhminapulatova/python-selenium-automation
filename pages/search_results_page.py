from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-index='2'][data-component-id='18']")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_subnav_locator(self, category):
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT)

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_selected_dept(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)
