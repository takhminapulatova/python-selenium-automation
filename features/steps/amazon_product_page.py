from selenium.webdriver.common.by import By
from behave import given, when, then


# ADD_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, "li.slots-hidden")
CURRENT_COLOR = (By.CSS_SELECTOR, ".inline-twister-dim-title-value")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Add the product to the cart')
def add_the_product(context):
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BTN)).click()
    context.app.product_page.click_add_to_cart()


@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors: ', all_color_options)
    expected_colors = ['Black', 'Army Green', 'Blue', 'Brown', 'Burgundy']

    actual_colors = []
    for color in all_color_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'


@then('Verify that user can click through all colors')
def verify_user_can_select_any_color(context):
    list_of_colors = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Khaki Brown', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed', 'Sage Green', 'Vintage Wash', 'Washed Black', 'Washed Grey']

    actual_colors = []
    for color in list_of_colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'


@then('Verify that the user sees the deals')
def verify_deals_are_visible(context):
    context.app.product_page.verify_deals_are_visible()
