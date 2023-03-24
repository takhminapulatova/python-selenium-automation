from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By. ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
# ORDERS = (By.ID, 'nav-orders')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_url()


@when('Input text {search_word}')
def input_search_word(context, search_word):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
    context.app.header.input_search_text(search_word)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click on orders')
def click_on_orders(context):
    # context.driver.find_element(*ORDERS).click()
    context.app.header.click_orders()


@when('Click Sign In from popup')
def click_signin(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in btn not clickable'
    ).click()


@when('Wait for {sec} seconds')
def wait_for_sec(context, sec):
    sleep(int(sec))


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@when('Select "Amazon Fresh" department')
def select_amazon_fresh_dept(context):
    context.app.header.select_amazon_fresh_dept()


@then('Verify Sign in popup shown')
def verify_signin_popup_visible(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in btn not clickable'
    )


@then('Verify Sign in popup disappears')
def verify_signin_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_BTN),
        message='Sign in btn did not disappear'
    )


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()


@when('Click on ham menu')
def click_ham_menu(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    context.ham_menu.click()


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(expected_amount)

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_links)
    # print('\nLink_count: ', len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected 42 links, but got {len(footer_links)}'


@then('Verify Spanish option present')
def verify_lang_shown(context):
    context.app.header.verify_lang_shown()
