from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import subprocess

# Step 1: Open Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()

# Step 2: Search for Latest News
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Latest News")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

# Step 3: Get top 5 video links
videos = driver.find_elements(By.XPATH, '//a[@id="video-title"]')[:5]
video_links = [video.get_attribute("href") for video in videos if video.get_attribute("href")]

# Step 4: Open Notepad
subprocess.Popen(['notepad.exe'])
time.sleep(1)  # wait for notepad to open

# Step 5: Paste the video links into Notepad
for link in video_links:
    pyautogui.typewrite(link + "\n\n", interval=0.05)

# Step 6: Close browser
driver.quit()
