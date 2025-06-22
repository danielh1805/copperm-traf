from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

url = "https://copperm.com/"
try:
    driver.set_page_load_timeout(20)
    driver.get(url)
    time.sleep(random.randint(10, 20))
finally:
    driver.quit()
