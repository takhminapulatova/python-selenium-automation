from selenium.webdriver.common.by import By
from behave import given, then


@given('Open Amazon Customer Service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify that UI elements are present')
def verify_elements_are_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.fs-heading")
    context.driver.find_element(By.CSS_SELECTOR, "div.issue-card-container")
    context.driver.find_element(By.CSS_SELECTOR, "label h2.fs-heading")
    context.driver.find_element(By.CSS_SELECTOR, "form.a-spacing-top-small")
    context.driver.find_element(By.XPATH, "//h2[contains(text(),'topics')]")
    context.driver.find_element(By.CSS_SELECTOR, "ul.help-topics")
