from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By. ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click Sign In from popup')
def click_signin(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()
    # Feel free to add error message if needed too, for example:
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGN_IN_BTN),
    #     message='Sign in btn not clickable'
    # ).click()


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    element = context.driver.find_element(*HAM_MENU)

@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    #print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    #print('Type after converting: ', type(expected_amount))

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_links)
    # print('\nLink_count: ', len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected 42 links, but got {len(footer_links)}'