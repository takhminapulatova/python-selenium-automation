from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/tahmina/Desktop/Careerist/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()
expected_result = True
actual_result = driver.find_element(By.XPATH, "//h1 [@class='a-spacing-small']").is_displayed()

assert expected_result == actual_result, f'Expected -> {expected_result} and actual -> {actual_result}'
driver.quit()
