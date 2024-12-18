from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://google.com"
driver.get(url)
driver.get("https://github.com/sadikturan")
#time.sleep(2)
#print(driver.title)
#driver.save_screenshot("selenium.png")
if "sadikturan" in driver.title:
    driver.maximize_window()
    driver.save_screenshot("sadikturan.png")
driver.back()
input("")
driver.close()