from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless") 

class Github:
    def __init__(self,username):
        self.username = username
        self.browser = webdriver.Chrome(options=options)
        self.followers = []

    def signIn(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
    
    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed ")
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary").text)

    def getFollowers(self):
        self.loadFollowers()
        found_next = False
        while True:
            links = self.browser.find_elements(By.CSS_SELECTOR,".pagination a")
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(3)
                    self.loadFollowers()
                    found_next = True
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(3)
                        self.loadFollowers()
                    else:
                        continue
            if not found_next:
                break

    def close(self):
        self.browser.quit()

    def textFile(self):
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in self.followers:
                file.write(item + "\n")

