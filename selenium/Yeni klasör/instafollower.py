from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class instagram:
    def __init__(self,username):
        self.username = username
        self.browser = webdriver.Chrome()

    def getlink(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(10)
    def close(self):
        self.browser.quit()

instagram = instagram("")
instagram.getlink()

instagram.close()