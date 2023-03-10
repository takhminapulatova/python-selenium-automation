from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href*='amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_terms_of_condition_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_on_privacy_notice(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('amazon.com/gp/help/customer'))


@then('User can close new window and switch back to original')
def close_window_switch_to_orig(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)