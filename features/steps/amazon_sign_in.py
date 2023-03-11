from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


@then('Verify that Sign In page is opened')
def verify_sign_in_opened(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    context.app.sign_in_page.verify_sign_in_page()
