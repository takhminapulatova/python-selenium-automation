from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def browser_init(context):
    """
    :param context: Behave context
    """
    service = Service('/Users/tahmina/Desktop/Careerist/python-selenium-automation/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()