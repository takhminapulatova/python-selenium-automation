from selenium.webdriver.common.by import By
from pages.base_page import Page


class Cart(Page):
    CART_IS_EMPTY = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')
    CHECKOUT = (By.CSS_SELECTOR, "input[value='Proceed to checkout']")

    def verify_cart_is_empty(self):
        self.verify_partial_text("Your Amazon Cart is empty", *self.CART_IS_EMPTY)

    def verify_cart_not_emtpy(self):
        self.element_is_displayed(*self.CHECKOUT)
