from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()

# Step 1: Open Amazon
driver.get("https://www.amazon.in")

# Step 2: Wait for the page to load
time.sleep(3)

# Step 3: Find the search box and search for "Android phones under 15000"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Android phones under 15000")
search_box.send_keys(Keys.RETURN)

# Step 4: Wait for search results to load
time.sleep(5)

# Optional: Print the title of the page
print("Page Title:", driver.title)

# Step 5: Close browser after 10 seconds
time.sleep(10)
driver.quit()
