from selenium.webdriver.common.by import By
from behave import when, then


ALL_PRODUCTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, ".s-image-square-aspect .s-image")
PRODUCT_NAME = (By.CSS_SELECTOR, ".a-spacing-base h2")


@when('Click on the first product')
def click_on_the_first_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-index='2'][data-component-id='18']").click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that each product has a name and an image')
def verify_product_has_a_name(context):
    all_products = context.driver.find_elements(*ALL_PRODUCTS)

    for product in all_products:
        assert product.find_element(*PRODUCT_NAME).is_displayed(), 'Product does not have a name'
        assert product.find_element(*PRODUCT_IMAGE).is_displayed(), 'Product does not have an image'
