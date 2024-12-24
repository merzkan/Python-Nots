import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")
liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li")
print(liste)

for item in liste:
    film_name = item.find("h3",{"class":"ipc-title__text"}).text
    rating = item.find("span",{"class":"ipc-rating-star--rating"}).text
    print(film_name,rating)




'''
# fake user agent oluşturmak için.

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent 
ua = UserAgent()
url = "https://www.imdb.com/chart/top/"

headers = {"User-Agent": ua.random}

html = requests.get(url, headers=headers).content

print(html)

'''