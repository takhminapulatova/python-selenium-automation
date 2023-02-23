from selenium.webdriver.common.by import By
from behave import when, then


@when('Click on the cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@when('Click on the first product')
def click_on_the_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-index='2'][data-component-id='18']").click()


@when('Add the product to the cart')
def add_the_product(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify that Amazon cart is empty')
def verify_cart_is_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    assert actual_result == expected_result, f'Expected result is {expected_result} but actual is {actual_result}'


@then('Verify that Amazon cart is not empty')
def verify_cart_is_not_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "input[value='Proceed to checkout']").is_displayed()
