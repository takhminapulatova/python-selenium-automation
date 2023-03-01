from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


ADD_CART_BTN = (By.ID, 'add-to-cart-button')


@when('Add the product to the cart')
def add_the_product(context):
    context.driver.find_element(*ADD_CART_BTN).click()
    sleep(2)
