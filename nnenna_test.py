import time

from selenium import webdriver
from selenium.webdriver.common.by import By

Username = "standard_user"
Password = "secret_sauce"

FirstName = "CHARLES"
LastName = "Derus"
PostalCode = "1230490"



driver= webdriver.Chrome()


driver.get("https://www.saucedemo.com/")
time.sleep(5)

#Landing page
driver.find_element(By.ID, "user-name").send_keys(Username) # UserName text field
time.sleep(2)
driver.find_element(By.ID, "password").send_keys(Password) # Password text field
time.sleep(2)
driver.find_element(By.ID,"login-button").click() #click login button
time.sleep(2)

# product page

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(2)

#checkout
driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
time.sleep(3)
driver.find_element(By.ID,"checkout").click()
time.sleep(2)

driver.find_element(By.ID,"first-name").send_keys(FirstName)
time.sleep(5)
driver.find_element(By.ID,"last-name").send_keys(LastName)
time.sleep(5)
driver.find_element(By.ID,"postal-code").send_keys(PostalCode)
time.sleep(5)
driver.find_element(By.ID,"continue").click()
time.sleep(5)
driver.find_element(By.ID, "finish").click()
time.sleep(5)
driver.find_element(By.ID,"back-to-products").click()
time.sleep(5)

#logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(5)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(5)