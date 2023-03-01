from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Amazon logo
driver.find_element(By.XPATH, "//i [@aria-label = 'Amazon']")

# Continue button
driver.find_element(By.ID, 'continue')

# Need help link
driver.find_element(By.XPATH, "//a [@role = 'button']")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# *Conditions of use link
driver.find_element(By.XPATH, "//a [contains(@href, 'notification_condition_of_use')]")

# *Privacy Notice link
driver.find_element(By.XPATH, "//a [contains(@href, 'notification_privacy_notice')]")
