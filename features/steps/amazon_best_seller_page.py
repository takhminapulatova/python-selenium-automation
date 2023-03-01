from selenium.webdriver.common.by import By
from behave import given, then


HEADER_BS_LINKS = (By.CSS_SELECTOR, "#zg_header li")


@given('Open Best Seller page')
def open_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify that header has {expected_num} links')
def verify_amount_of_links(context, expected_num):
    expected_num = int(expected_num)
    header_bs_links = context.driver.find_elements(*HEADER_BS_LINKS)
    assert len(header_bs_links) == expected_num, f'Expected 5 links, but got {len(header_bs_links)}'


