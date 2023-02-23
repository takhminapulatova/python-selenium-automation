from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name field
driver.find_element(By.ID, 'ap_customer_name')

# Email field
driver.find_element(By.ID, 'ap_email')

# Password field
driver.find_element(By.ID, 'ap_password')

# Passwords req
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-inline-info')

# Re-enter password field
driver.find_element(By.ID, 'ap_password_check')

# Create account button
driver.find_element(By.ID, 'continue')

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy']")

# Sign In
driver.find_element(By.CSS_SELECTOR, "a[href*='signin']")
