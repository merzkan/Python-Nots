#BeautifulSoup module
'''
BeautifulSoup, Python'da kullanılan popüler bir kütüphane olup HTML ve XML dosyalarını kolayca parse etmek (ayrıştırmak)
ve bu belgelerden bilgi çekmek için kullanılır. Web scraping (web kazıma) işlemlerinde sıkça tercih edilir.

Neden Kullanılır?
1.Web Scraping (Web Kazıma):
Web sitelerindeki verileri otomatik olarak çekmek ve bu verilerle çalışmak için kullanılır.

2.HTML Manipülasyonu:
HTML belgelerini analiz edip değiştirmek için kullanılabilir.

3.Belirli Bilgilere Ulaşma:
Bir web sayfasındaki belirli bir başlık, tablo, bağlantı ya da başka bir bilgiyi bulmak için kullanılır.

'''

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">
    
    [<a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
    <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
    <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>]

</body>
</html>

"""
soup = BeautifulSoup(html_doc,"html.parser")


result = soup.prettify() # düzenler
result = soup.title #title kısmını getirir
#<title>İlk web sayfam</title>
result = soup.head #had kısmı gelir
result = soup.body

print("*****************************")

result = soup.title.name
#title
result = soup.title.string
#İlk web sayfam
result = soup.h1
#<h1 id="header">    
#       Python Kursu
#    </h1>
result = soup.h2 # ilk h2yi getirir.
result = soup.h2.name
#h2
result = soup.h2.string
#            Programlama

print("*****************************")


result = soup.find_all("h2") # bütün h2leri getirir.
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1] 

print("*****************************")

result = soup.div #ilk div gelir
result = soup.find_all("div") # hepsi gelir
result = soup.find_all("div")[1] #ikinci div gelir
result = soup.find_all("div")[1].ul #ikinci div altındaki ul etiketi
#<ul>
#<li>Menü 1</li>
#<li>Menü 2</li>
#<li>Menü 3</li>
#</ul>
result = soup.find_all("div")[1].ul.li
#<li>Menü 1</li>
result = soup.find_all("div")[1].ul.find_all("li")
#[<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]

print("*****************************")

result = soup.div.findChildren() # bütün alt elemanları gelir
#[<h2>
#            Programlama      
#        </h2>, <ul>
#<li>Menü 1</li>
#<li>Menü 2</li>
#<li>Menü 3</li>
#</ul>, <li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]
result = soup.div.find_next_sibling() # bir sonraki div
#<div class="grup2">
#<h2>
#            Modüller
#        </h2>
#<ul>
#<li>Menü 1</li>
#<li>Menü 2</li>
#<li>Menü 3</li>
#</ul>
#</div>
result = soup.div.find_next_sibling().find_next_sibling()#3.div gelir 
#<div class="grup3">
#<h2>
#            Django
#        </h2>
#<ul>
#<li>Menü 1</li>
#<li>Menü 2</li>
#<li>Menü 3</li>
#</ul>
#</div>
result = soup.div.find_next_sibling().find_next_sibling().find_previous_sibling() #3.divden 2.dive geçer
#<div class="grup2">
#<h2>
#            Modüller
#        </h2>
#<ul>
#<li>Menü 1</li>
#<li>Menü 2</li>
#<li>Menü 3</li>
#</ul>
#</div>


print("*****************************")

result = soup.find_all("a")

for link in result:
    print(link.get("href"))


print(result)