import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"})

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip('TL')
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip('TL')

    print(f"name: {name} link: {link} old price: {oldprice} new price: {newprice}")