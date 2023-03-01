from selenium.webdriver.common.by import By
from behave import when, then


@when('Click on the first product')
def click_on_the_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-index='2'][data-component-id='18']").click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
