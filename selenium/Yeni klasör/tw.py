from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://x.com/elonmusk"
driver.get(url)
time.sleep(5)

for i in range(0, 10):
    driver.execute_script("window.scrollBy(0, 1000);")  # 1000 piksel aşağı kaydır
    ss_name = f"elonmusk_{i}.png"
    driver.save_screenshot(ss_name)
    time.sleep(1)
driver.close()

