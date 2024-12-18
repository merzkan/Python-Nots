'''

NumPy, hızlı ve verimli sayısal hesaplamalar yapmak için kullanılır.

1. Temel Amaç:
Temelde sayısal hesaplamalar ve çok boyutlu diziler (arrays) için geliştirilmiştir. 
Matris işlemleri, lineer cebir, istatistik ve diğer matematiksel işlemler için optimize edilmiştir.

2. Veri Yapıları
Tek bir veri yapısı sunar: ndarray (n boyutlu dizi).
Homojen veri tiplerini destekler, yani bir NumPy dizisi içindeki tüm öğeler aynı veri tipinde olmalıdır
(ör. tüm elemanlar float veya int olmalı).

3. Performans
NumPy, daha düşük seviyede çalıştığı ve doğrudan belleği yönetebildiği için daha hızlıdır.
Büyük boyutlu sayısal işlemler ve matris hesaplamaları için idealdir.

4. Veri Manipülasyonu ve Analizi
Temel matematiksel ve istatistiksel işlemler yapılır.
Veri manipülasyonu için daha fazla manuel işlem gerekir.

5. Veri Kaynaklarıyla Çalışma
Veri dosyalarını doğrudan işlemek için tasarlanmamıştır.
Veriler genellikle diğer kaynaklardan yüklenir ve NumPy'ye dönüştürülür.
'''
import numpy as np

py_list = [1,2,3,4,5,6,7,8,9]
np_array = np.array([1,2,3,4,5,6,7,8,9])


py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)


print(py_multi)#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np_multi)
#[[1 2 3]
#[4 5 6]
#[7 8 9]]
print("*******************************")
print(type(py_list))#<class 'list'>
print(type(np_array))#<class 'numpy.ndarray'>
print("*******************************")
print(np_array.ndim)#1 boyutu
print(np_multi.ndim)#2 boyutu
print("*******************************")
print(np_array.shape)#(9,)
print(np_multi.shape)#(3, 3)
