import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration
URL = "https://copperm.com/metals/metal.html?metal=copper"
START_HOUR = 7
END_HOUR = 15

def should_visit_now():
    from datetime import datetime
    hour = datetime.utcnow().hour + 3  # Adjust for Israel time
    return START_HOUR <= hour < END_HOUR

def main():
    total_visits = random.randint(100, 150)
    print(f"📅 Planned visits for today: {total_visits}")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 800)

    visits_done = 0
    for i in range(total_visits):
        if not should_visit_now():
            print("⏸️ Outside of allowed hours (07:00–15:00). Skipping visit.")
            continue

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
