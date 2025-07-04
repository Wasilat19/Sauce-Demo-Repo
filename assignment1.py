rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time

#Setup Webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#Navigate to the Sauce demo website
driver.get("https://saucedemo.com/inventory.html")
wait = WebDriverWait(driver, 10)

#Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#Add all six products to the cart using a loop
add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
for button in add_to_cart_buttons:
    button.click()
    total_items_added = len (add_to_cart_buttons)
    print(f"✅ Added {total_items_added} products to cart.")

#Log out
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)  # Give time for menu animation
driver.find_element(By.ID, "logout_sidebar_link").click()

#Close browser
time.sleep(2)
driver.quit()
