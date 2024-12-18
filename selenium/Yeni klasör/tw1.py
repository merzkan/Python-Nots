from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://x.com/elonmusk"
driver.get(url)

result =driver.find_element(By.CSS_SELECTOR,"span")

for i in result:
    print(i)

driver.close()

