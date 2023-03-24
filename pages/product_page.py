from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class Product(Page):
    ADD_CART_BTN = (By.ID, 'add-to-cart-button')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[aria-label='New Arrivals']")
    DEALS_MENU = (By.CSS_SELECTOR, "div.mega-menu")

    def click_add_to_cart(self):
        self.click(*self.ADD_CART_BTN)

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_deals_are_visible(self):
        self.wait_for_element_appear(*self.DEALS_MENU)
