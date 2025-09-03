from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize Chrome browser
driver = webdriver.Chrome()

# Step 1: Open YouTube
driver.get("https://www.youtube.com")

# Step 2: Wait for page to load
time.sleep(3)

# Step 3: Find the search box and search for "David Guetta songs"
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("David Guetta songs")
search_box.send_keys(Keys.RETURN)

# Step 4: Wait for results to load
time.sleep(5)

# Step 5: Click the first video in search results
first_video = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
first_video.click()

# Step 6: Let the video play for 20 seconds before closing
time.sleep(20)

# Close browser
driver.quit()
