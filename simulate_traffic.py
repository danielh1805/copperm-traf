from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime

# רשימת עמודי כניסה
pages = [
    "https://copperm.com/",
    "https://copperm.com/metals/metal.html?metal=aluminum",
    "https://copperm.com/metals/metal.html?metal=copper",
    "https://copperm.com/metals/metal.html?metal=iron"
]

# הגדרות דפדפן
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# יצירת הדפדפן
driver = webdriver.Chrome(options=options)

visits = random.randint(4, 7)  # הרצת מספר גולשים אמיתיים

print(f"🟢 Simulating {visits} user visits...
")

for i in range(visits):
    try:
        url = random.choice(pages)
        driver.get(url)
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{now} | Visit {i+1}: {url}")

        # שוהה באתר בין 30 ל-120 שניות
        wait_time = random.randint(30, 120)
        print(f"    ⏳ Waiting {wait_time} seconds...")
        time.sleep(wait_time)

        # נסה ללחוץ על לינק פנימי אקראי
        links = driver.find_elements(By.TAG_NAME, "a")
        internal_links = [a.get_attribute('href') for a in links if a.get_attribute('href') and 'copperm.com' in a.get_attribute('href')]
        if internal_links:
            next_url = random.choice(internal_links)
            print(f"    🔗 Clicking on: {next_url}")
            driver.get(next_url)
            second_wait = random.randint(20, 60)
            print(f"    ⏳ Waiting another {second_wait} seconds...")
            time.sleep(second_wait)

    except Exception as e:
        print(f"    ❌ Error: {e}")

driver.quit()
