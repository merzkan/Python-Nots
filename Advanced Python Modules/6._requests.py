#requests module
'''
requests modülü,
Python'da HTTP protokolü kullanarak web ile iletişim kurmayı sağlayan güçlü ve popüler bir kütüphanedir.
Kullanımı basit ve esnektir, özellikle API'lerle çalışırken veya internette veri alıp göndermek istediğinizde büyük kolaylık sağlar. 
requests, Python'daki standart HTTP modülü olan urllib'ye göre daha kullanıcı dostudur.

Temel Özellikler
GET, POST, PUT, DELETE, PATCH gibi tüm HTTP istek türlerini destekler.
JSON veri formatıyla kolayca çalışabilir.
Çerez yönetimi yapabilir.
Zaman aşımı ve yeniden deneme mekanizmalarını destekler.
HTTPS gibi güvenli bağlantılarla çalışabilir

Neden Kullanılır?
Web sayfalarından veri çekmek (web scraping).
REST API'lerle iletişim kurmak.
Dosya indirmek veya yüklemek.
Web servislerine veri göndermek veya almak.

--------------------------------------------------------------------------------------------------------

REST API Nedir?
REST API (Representational State Transfer - Application Programming Interface)
web servisleriyle iletişim kurmak için kullanılan bir mimari tarzdır. 
internet üzerinden farklı uygulamalar arasında veri alışverişi yapılmasını sağlar.

REST'in Temel İlkeleri:
1.Kaynaklar(Resources):REST API, sistemdeki veri varlıklarını "kaynaklar" olarak tanımlar (örneğin, bir kullanıcı, ürün, makale).

2.HTTP Metodları: REST API, veri işlemleri için genellikle şu HTTP metodlarını kullanır:
GET: Veriyi almak için.
POST: Yeni bir veri eklemek için.
PUT: Var olan bir veriyi güncellemek için.
DELETE: Bir veriyi silmek için.

3.Stateless (Durumsuzluk): Her istek bağımsızdır; API sunucusu, önceki isteklerin bağlamını hatırlamaz.
4.JSON Formatı: Veri alışverişi genellikle JSON formatında yapılır.

--------------------------------------------------------------------------------------------------------

API, bir uygulamanın başka bir uygulamayla iletişim kurmasını ve belirli işlevlerini kullanmasını sağlayan bir ara yüzdür.
API, "Application Programming Interface" (Uygulama Programlama Arayüzü) teriminin kısaltmasıdır. 
API, yazılımların birbiriyle iletişim kurmasını sağlayan bir ara yüzdür.
bir yazılımın, başka bir yazılımın işlevlerine veya verilerine erişmesi ve onları kullanması için standartlaştırılmış bir yöntem sunar.

API'nin İşlevi:
API, bir yazılımın başka bir yazılımın özelliklerini veya hizmetlerini kullanmasını sağlar.
Bu, genellikle internet üzerinden, bir istemci (örneğin, bir mobil uygulama) ve bir sunucu (örneğin, bir web hizmeti) arasında gerçekleşir.
Örneğin:
Bir hava durumu uygulaması, hava durumu verilerini bir API aracılığıyla alır.
Bir e-ticaret sitesi, ödeme işlemlerini gerçekleştirmek için bir banka API'sini kullanır.

API'nin Çalışma Mantığı
İstemci (Client): Bir API'ye istek gönderir (örneğin, hava durumu bilgisi ister).
Sunucu (Server): Bu isteği işler, gerekli bilgileri bulur ve istemciye bir yanıt döner.
Yanıt (Response): Sunucu, genellikle JSON veya XML formatında veri döner.

API Türleri
1.Web API'ler (RESTful API):
Web üzerinden çalışan API'lerdir.
Örneğin: Hava durumu API'leri, sosyal medya API'leri (Facebook, Twitter).

2.Kütüphane API'leri:
Bir programlama dili veya kütüphanenin sunduğu işlevlere erişim sağlar.
Örneğin: Python math modülü.

3.Donanım API'leri:
Bir donanım aygıtı ile iletişim kurmak için kullanılır.
Örneğin: Kamera veya ses kartı API'leri.

4.İşletim Sistemi API'leri:
İşletim sistemi seviyesindeki işlemleri gerçekleştirmek için kullanılır.
Örneğin: Windows API, POSIX API.
'''
import requests
import json


result = requests.get("https://jsonplaceholder.typicode.com/todos")
#<Response [200]>    # başarılı bir sonucun geldigini gösteriyor
result1 = result.text
print(result)
#print(result1)
print(type(result))
#<class 'requests.models.Response'>
print(type(result1))
#<class 'str'>

result2 = json.loads(result.text)

print(result2[0]["title"])
#delectus aut autem
print(result2[0])
#{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

#print(result2) #tüm bilgileri yazdırır

for i in result2: #satır satır geldi
    if i["userId"] == 1:
        print(i["title"])