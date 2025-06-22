from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# הגדרת כתובת האתר שלך
url = "https://copperm.com"

# הגדרת אפשרויות הדפדפן
options = Options()
options.add_argument("--headless")  # ריצה ללא GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("🚀 Launching Chrome browser...")

# יצירת מופע דפדפן
driver = webdriver.Chrome(options=options)

print(f"🌐 Visiting: {url}")
driver.get(url)

# הדפסת כותרת הדף לוודא טעינה
print(f"📄 Page title: {driver.title}")

# השהייה של 5 שניות לדמות ביקור
time.sleep(5)

print("✅ Visit complete. Closing browser.")
driver.quit()
