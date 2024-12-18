'''

Pandas, tablo şeklinde yapılandırılmış veriler üzerinde veri analizi ve manipülasyonu için idealdir.

1. Temel Amaç
 Veri analizi ve veri manipülasyonu için tasarlanmıştır. Yapılandırılmış veriler 
(tablo formatında veri) üzerinde çalışmaya odaklanır.

2. Veri Yapıları
İki ana veri yapısı sunar:
Series: Tek boyutlu veri yapısı (indekslenmiş bir NumPy dizisine benzer).
DataFrame: Satır ve sütunlardan oluşan iki boyutlu bir veri yapısı (Excel tablosuna benzer).
Heterojen veri tiplerini destekler, yani bir DataFrame'in farklı sütunları farklı veri tiplerine sahip olabilir 
(ör. bir sütun int, diğer sütun string olabilir).

3. Performans
Pandas, esneklik ve kullanım kolaylığı sağlar ancak performansı NumPy'ye göre biraz daha düşüktür.
Veri analizi ve manipülasyonunda daha kullanıcı dostudur.

4. Veri Manipülasyonu ve Analizi
Veri analizi ve manipülasyonu için çok sayıda yerleşik yöntem sunar.
Eksik veri yönetimi (NA değerleri doldurma/silme), gruplama, sıralama, birleştirme ve pivot tablolar gibi 
işlemleri kolayca gerçekleştirebilir.

5. Veri Kaynaklarıyla Çalışma
CSV, Excel, SQL, JSON ve daha birçok veri formatını doğrudan okuyabilir ve kaydedebilir. 
Bu, Pandas'ı yapılandırılmış verilerle çalışmak için ideal hale getirir.
'''
#pandas serileri(Series)
import pandas as pd
import numpy as np

pandas_series = pd.Series([10,20,30,40])
print(pandas_series)
#0    10     
#1    20     
#2    30     
#3    40     
#dtype: int64
print(pandas_series.ndim) # 1 boyutu
print(pandas_series.dtype) # int64
print(pandas_series.shape) #(4,)
print(pandas_series.sum()) #100
print(pandas_series.max()) #40
print(pandas_series.min()) #10
print(pandas_series+pandas_series)
#0    20
#1    40
#2    60
#3    80
#dtype: int64
print(pandas_series+50)
#0    60
#1    70
#2    80
#3    90
#dtype: int64
print(pandas_series >=50)
#0    False
#1    False
#2    False
#3    False
#dtype: bool
print(pandas_series[pandas_series >=50])
#Series([], dtype: int64) 50den büyük sayı olmadıgı için olsa yazardı.
print("******************")

numbers = [20,30,40,50]
letters = ['a','b','c',20] #heterojen yapı
scalar = 5

pandas_series1 = pd.Series(numbers)
pandas_series2 = pd.Series(letters)
pandas_series3 = pd.Series(scalar)
pandas_series4 = pd.Series(5,[0,1,2,3])
pandas_series5 = pd.Series(numbers,['a','b','c','d']) #eleman sayıları aynı olması gerekiyor.
print(pandas_series1)
#0    20
#1    30
#2    40
#3    50
#dtype: int64 
print(pandas_series2)
#0    a
#1    b
#2    c
#3    20
#dtype: object
print(pandas_series3)
#0    5
#dtype: int64
print(pandas_series4)
#0    5
#1    5
#2    5
#3    5
#dtype: int64
print(pandas_series5)
#a    20
#b    30
#c    40
#d    50
#dtype: int64

print("******************")

dict = {'a':10,'b':20,'c':30,'d':40}
pandas_series6 = pd.Series(dict)

print(pandas_series6)
#a    10
#b    20
#c    30
#d    40
#dtype: int64

print("******************")

random_numbers = np.random.randint(10,100,6)

pandas_series7 = pd.Series(random_numbers)

print(pandas_series7)
#0    28
#1    33
#2    20
#3    33
#4    76
#5    45
#dtype: int32

print("******************")

pandas_series8 = pd.Series([20,30,40,50],['a','b','c','d'])

result = pandas_series8.iloc[0]#Pozisyona Göre Erişim (Position-Based)
result1 = pandas_series8['a']#Etikete Göre Erişim (Label-Based)
result2 = pandas_series8.iloc[:2]
result3 = pandas_series8.iloc[-2:]
result4 = pandas_series8[['a','c']]
#result5 = pandas_series8[['a','c','e']]
result6 = pandas_series8[pandas_series8.index.isin(['a','c','e'])]
result7 = pandas_series8.reindex(['a','c','e'])
print(result)#20
print(result1)#20
print(result2)
#a    20
#b    30
#dtype: int64
print(result3)
#c    40
#d    50
#dtype: int64
print(result4)
#a    20
#c    40
#dtype: int64

#print(result5)
#hata verir eski sürümünde çalışıyor.
print(result6)
#a    20
#c    40
#dtype: int64
print(result7)
#a    20.0
#c    40.0
#e     NaN
#dtype: float64

print("*********************")

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019

print(total)
#astra        60.0
#corsa        60.0
#grandland     NaN
#insignia     20.0
#mokka         NaN
#dtype: float64
print(total["astra"]) #60.0
#print(total["combo"]) hata verir

#pandas serileri