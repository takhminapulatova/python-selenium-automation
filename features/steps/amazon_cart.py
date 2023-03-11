from selenium.webdriver.common.by import By
from behave import when, then


# CART_ICON = (By.ID, 'nav-cart-count-container')


@when('Click on the cart icon')
def click_on_cart_icon(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart_icon()


@then('Verify that Amazon cart is empty')
def verify_cart_is_empty(context):
    # expected_result = "Your Amazon Cart is empty"
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    # assert actual_result == expected_result, f'Expected result is {expected_result} but actual is {actual_result}'
    context.app.cart_page.verify_cart_is_empty()


@then('Verify that Amazon cart is not empty')
def verify_cart_is_not_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "input[value='Proceed to checkout']").is_displayed()
    # context.app.cart_page.verify_cart_not_empty()
