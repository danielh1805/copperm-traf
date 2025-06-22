import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration
URL = "https://copperm.com/"
TOTAL_VISITS = random.randint(100, 150)

def main():
    print(f"📅 Planned visits for today: {TOTAL_VISITS}")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)

    visits_done = 0
    for i in range(TOTAL_VISITS):
        try:
            print(f"🔗 Visit {i+1}: {URL}")
            driver.get(URL)
            wait_time = random.randint(40, 60)
            print(f"⏳ Staying on page for {wait_time} seconds...")
            time.sleep(wait_time)
            visits_done += 1
        except Exception as e:
            print(f"❌ Error: {e}")

    driver.quit()
    print(f"✅ Total visits completed: {visits_done}")

if __name__ == "__main__":
    main()
