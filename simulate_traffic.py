import time, random, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def simulate_human(driver):
    action = ActionChains(driver)
    x = random.randint(100, 800)
    y = random.randint(100, 600)
    action.move_by_offset(x, y).perform()
    time.sleep(random.uniform(0.5, 2))
    action.move_by_offset(-x/2, -y/2).perform()
    time.sleep(random.uniform(0.5, 2))

def main():
    with open('links.json') as f:
        links = json.load(f)
    visits = random.randint(70, 100)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    for i in range(visits):
        url = random.choice(links)
        print(f"🔗 Visit {i+1}: {url}")
        try:
            driver.get(url)
            time.sleep(random.uniform(5, 15))
            simulate_human(driver)
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 5))
        except Exception as e:
            print(f"❌ Error visiting {url}: {e}")
    driver.quit()

if __name__ == '__main__':
    main()
