from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

@when('Click on orders')
def click_on_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify that Sign In page is opened')
def verify_sign_in_page(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').is_displayed(), 'Sign In header is present'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email input field is present'


@then('Verify Sign In page opens')
def verify_signin_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))