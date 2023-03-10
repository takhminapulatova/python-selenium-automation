from selenium.webdriver.common.by import By
from behave import given, then


HEADER_BS_LINKS = (By.CSS_SELECTOR, "#zg_header li")
TITLE = (By.CSS_SELECTOR, "#zg_banner_text")


@given('Open Best Seller page')
def open_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify that header has {expected_num} links')
def verify_amount_of_links(context, expected_num):
    expected_num = int(expected_num)
    header_bs_links = context.driver.find_elements(*HEADER_BS_LINKS)
    assert len(header_bs_links) == expected_num, f'Expected 5 links, but got {len(header_bs_links)}'


@then('Verify that each link opens correct page')
def verify_each_link_open_correct_page(context):
    header_bs_links = context.driver.find_elements(*HEADER_BS_LINKS)
    for i in range(len(header_bs_links)):
        link = context.driver.find_elements(*HEADER_BS_LINKS)[i]
        header_name = link.text
        # print(header_name)
        link.click()
        title = context.driver.find_element(*TITLE).text
        # print(title)
        assert header_name in title, f'Expected header name: {header_name} is in the title: {title}'
