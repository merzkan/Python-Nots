from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://www.google.com.tr/?hl=tr"
driver.get(url)

searchInput = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
searchInput.clear()
searchInput.send_keys("python")
searchInput.send_keys(Keys.RETURN)

tikla = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
tikla.click()

tikla1 = driver.find_element(By.XPATH,"//*[@id='documentation']/a")
tikla1.click()

tikla2 = driver.find_element(By.XPATH,"//*[@id='touchnav-wrapper']/header/div/div[2]/div/p[3]/a")
tikla2.click()


result = driver.find_elements(By.CSS_SELECTOR,"a.biglink")

for element in result:
    print(element.text)

time.sleep(2)
driver.close()
