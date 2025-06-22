
from selenium import webdriver
import time
import random
from selenium.webdriver.chrome.options import Options

url = "https://copperm.com/"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    for i in range(3):  # Only 3 visits for testing
        print(f"🔁 Visit {i+1}: {url}")
        driver.get(url)
        print(f"✅ Page title: {driver.title}")
        time.sleep(random.uniform(10, 20))  # Short stay for test
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    driver.quit()
    print("🏁 Finished test run.")
