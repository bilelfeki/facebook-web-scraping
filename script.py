import requests
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from concurrent.futures import ThreadPoolExecutor

# Define the cookies
cookies = {
    'c_user': '',
    'datr': '',
    'fr' : '',
    'presence' : '',
    'ps_l': '',
    'ps_n': '',
    'ps_n' : '',
    'sb':'',
    'wd':'',
    'xs' : ''
}

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Required for some environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

urls = [
    "https://www.facebook.com/groups/649261791870998/?sorting_setting=CHRONOLOGICAL",
    "https://www.facebook.com/groups/814597532008792/?sorting_setting=CHRONOLOGICAL",

    "https://www.facebook.com/groups/139068829520415/?sorting_setting=CHRONOLOGICAL"

]


def vistUrl(url):
  try:
    # Navigate to the base URL (necessary before adding cookies)

    # Navigate to the target URL
    driver.get(url)
    # Print the page title to verify the request succeeded
    for _ in range(5):  # Adjust the range for more scrolls
          driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down by 1000 pixels
          time.sleep(2)# Pause to allow dynamic content to load


    try:
        feed_div = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
        #print("Found the div:", feed_div)
        feed_html = feed_div.get_attribute("outerHTML")
        story_messages = feed_div.find_elements(By.CSS_SELECTOR, '[data-ad-rendering-role="story_message"]')
        story_texts = [message.text for message in story_messages]

        profile_names = feed_div.find_elements(By.CSS_SELECTOR, '[data-ad-rendering-role="profile_name"]')
        profile_texts = [name.text for name in profile_names]
        # Print extracted texts
        for profile, story in zip(profile_texts, story_texts):
          print(f"Profile Name: {profile}")
          print(f"Story Message: {story}")
          print("-" * 40)  # Separator for clarity


    except:
        print("Div with role='feed' not found.")
  finally:
      print('ok')

for url in urls:
    # Add cookies to the browser
    driver = webdriver.Chrome(options=chrome_options)
    for name, value in cookies.items():
        driver.get("https://www.facebook.com")
        driver.add_cookie({"name": name, "value": value})
    vistUrl(url)
driver.quit()