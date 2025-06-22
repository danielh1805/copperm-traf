from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
# options.add_argument('--headless')  # השאר מבוטל בשלב זה
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

print("🚀 Launching Chrome browser...")
driver = webdriver.Chrome(options=options)

try:
    driver.set_page_load_timeout(20)
    url = "https://copperm.com/"
    print(f"🌐 Visiting {url}")
    driver.get(url)

    print("⏳ Waiting for page to load...")
    time.sleep(5)

    print("📜 Scrolling to bottom of the page...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    print("🖱️ Trying to click on body element...")
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        ActionChains(driver).move_to_element(body).click().perform()
        print("✅ Click performed.")
        time.sleep(2)
    except Exception as e:
        print(f"⚠️ Could not click: {e}")

    print("⏳ Waiting to let Google Analytics register the visit...")
    time.sleep(10)

    print("✅ Visit simulation complete.")

finally:
    print("🧹 Closing browser.")
    driver.quit()
