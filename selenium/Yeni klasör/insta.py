from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://www.instagram.com/"
driver.get(url)

name = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
password = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
button = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')

name.send_keys("merhaba")
password.send_keys("123456789")
button.click()


driver.close()