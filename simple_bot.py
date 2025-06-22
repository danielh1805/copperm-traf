from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, random

URL = "https://copperm.com/"
VISITS = 3  # small number for testing

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = '/usr/bin/google-chrome'

driver = webdriver.Chrome(options=chrome_options)

try:
    for i in range(VISITS):
        print(f"🔗 Visit {i+1}: {URL}")
        driver.get(URL)
        print(f"    Page title: {driver.title}")
        wait = random.uniform(10, 20)
        print(f"    ⏳ Waiting {wait:.1f} seconds")
        time.sleep(wait)
finally:
    driver.quit()
    print("🏁 Finished run.")
