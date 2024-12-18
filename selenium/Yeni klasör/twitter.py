from twitteruserinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import time
import os

class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()  
        self.username = username
        self.password = password

    def load_cookies(self):
        if os.path.exists("twitter_cookies.pkl"):
            with open("twitter_cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                self.browser.get("https://x.com")
                for cookie in cookies:
                    self.browser.add_cookie(cookie)
                return True
        return False

    def sigIN(self):
        # Eğer çerezler yüklendiyse, giriş yapmaya gerek yok
        if not self.load_cookies():
            self.browser.get("https://x.com/i/flow/login")
            time.sleep(2)

            usernameInput = self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
            usernameInput.send_keys(self.username)
            usernameInput.send_keys(Keys.RETURN)
            time.sleep(2)

            passwordInput = self.browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")                                                                                      
            passwordInput.send_keys(self.password)
            
            self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/button/div/span/span").click()

            time.sleep(5)
            self.save_cookies()

    def save_cookies(self):
        cookies = self.browser.get_cookies()
        with open("twitter_cookies.pkl", "wb") as file:
            pickle.dump(cookies, file)
        print("Çerezler kaydedildi.")

    def close_browser(self):
        self.browser.quit()

# Twitter sınıfını başlatıyoruz ve giriş yapıyoruz
twitter = Twitter(username, password)
twitter.sigIN()
twitter.close_browser()
