#os module
'''
os module(operating system)

Python os modülü, işletim sistemi ile etkileşim kurmanıza olanak tanıyan bir modüldür. 
Bu modül, dosya ve dizin işlemleri yapmayı, işletim sistemi bilgilerine erişmeyi ve sistemle ilgili çeşitli görevleri yerine getirmeyi sağlar. 
os modülünün sunduğu bazı temel işlevler şunlardır:

1.Dosya ve Dizin İşlemleri
os.mkdir(path): Belirtilen dizini oluşturur.
os.makedirs(path): Gerekirse birden fazla dizin oluşturur.
os.remove(path): Belirtilen dosyayı siler.
os.rmdir(path): Boş dizini siler.
os.removedirs(path): Boş dizinleri ve gerekli alt dizinleri siler.
os.rename(old, new): Dosya veya dizini yeniden adlandırır.

2.Dosya ve Dizin İşlemleri
os.mkdir(path): Belirtilen dizini oluşturur.
os.makedirs(path): Gerekirse birden fazla dizin oluşturur.
os.remove(path): Belirtilen dosyayı siler.
os.rmdir(path): Boş dizini siler.
os.removedirs(path): Boş dizinleri ve gerekli alt dizinleri siler.
os.rename(old, new): Dosya veya dizini yeniden adlandırır.

3.Yol İşlemleri
os.path.join(path, *paths): Birden fazla yolu doğru bir şekilde birleştirir.
os.path.exists(path): Verilen yolun var olup olmadığını kontrol eder.
os.path.isdir(path): Verilen yolun bir dizin olup olmadığını kontrol eder.
os.path.isfile(path): Verilen yolun bir dosya olup olmadığını kontrol eder.
os.path.abspath(path): Verilen yolun tam (absolut) yolunu döndürür.

4.Çevresel Değişkenler
os.environ: Çevresel değişkenlere erişim sağlar (örneğin, sistemdeki kullanıcı bilgileri, yol ayarları vb.).
os.getenv(key): Çevresel bir değişkenin değerini döndürür.
os.putenv(key, value): Çevresel bir değişkenin değerini ayarlar.

5. Çalışma Dizini
os.getcwd(): Mevcut çalışma dizinini döndürür.
os.chdir(path): Çalışma dizinini değiştirir.

6. Sistem Bilgileri
os.uname(): (Unix tabanlı sistemlerde) Sistem hakkında bilgi döndürür.
os.system(command): Sistem komutları çalıştırmak için kullanılır. (Bu fonksiyon, bir komut satırı komutunu çalıştırmanıza olanak tanır.)

7. Process (İşlem) Yönetimi
os.getpid(): Şu anda çalışan işlemin kimliğini (PID) döndürür.
os.fork(): Bir işlem oluşturur (Unix tabanlı sistemlerde geçerlidir).

'''
import os
import datetime

result1 = dir(os) #class ve methodları listeler
#print1(result)

result2 = os.name#işletim sistemini söyler nt= windows
#nt
result3 = os.getcwd()#dosya hakkında bilgi verir hangi klasörde
#C:\Users\omerozkan\Desktop\Cod\python\Advanced Python Modules

print(result2)
print(result3)

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('..')
# os.chdir('../..') #iki defa üst dizine geçme

# klasör oluşturma
# os.mkdir("newdirectory") # yeni klasör oluşturma
# os.makedirs("newdirectory/yeniklasör") #iç içe klasör oluşturma
# os.rename("newdirectory","yeniklasör") # klasörün adını değiştirme
# os.rmdir("newdirectory") # klasörü silme
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir() #şu an etkili olan dizindeki klasörleri listeler
# result = os.listdir('C:\\') #konumunu belirtip o konumdaki klasörler listeler
# for dosya in os.listdir(): #sadece py uzantılı dosyaları listeler
#     if dosya.endswith('.py'):
#         print(dosya)


#result = os.stat("2.py")#bilgi sahib oluruz
#os.stat_result(st_mode=33206, st_ino=10414574138589828, st_dev=10960282242307226678, st_nlink=1, st_uid=0, st_gid=0, st_size=3692, st_atime=1734964322, st_mtime=1734964321, st_ctime=1734963194)

#result = result.st_size/1024 #kb türündde bilgi sahibi oluruz
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

#os.system("notepad.exe") #notepad açar

print("************************************")

# path

result = os.path.abspath("_os.py") #dosyanın tam konumunu verir
result = os.path.dirname("C:/python/advanced-modules/_os.py")#dizin ismini verir
result = os.path.dirname(os.path.abspath("_os.py")) #dizin ismini verir
result = os.path.exists("C:/python/advanced-modules/_os1.py") #var mı yok mu true false verir  
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules")#klasör mü değil mi true false
result = os.path.isfile("C:/python/advanced-modules/_os.py")#dosya mı degıl mı true false
result = os.path.join("C:\\","deneme","deneme1")#dızın olusturma
result = os.path.split("C:\\deneme")#path bılgılerını bolmek ıcın
result = os.path.splitext("_os.py")#dosyanın ısmıyle uzantısını ayırır

