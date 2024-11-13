from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--start-maximized")

driver = webdriver.Edge(options=edge_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    lang_eng = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
finally:
    lang_eng.click()

try:
    cookie = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
finally:
    total_timeout = time.time() + 5 * 60
    while True:
        try:
            available_products = driver.find_elements(
                By.CSS_SELECTOR, ".product.unlocked.enabled, .crate.upgrade.enabled"
            )
            random.choice(available_products).click()
        except:
            pass
        timeout = time.time() + 5
        while True:
            cookie.click()
            if time.time() > timeout:
                break
        if time.time() > total_timeout:
            break
cookies_rate = driver.find_element(By.ID, "cookiesPerSecond")
print(f"cookies {cookies_rate.text}")
driver.quit()
