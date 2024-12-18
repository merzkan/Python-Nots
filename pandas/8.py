#kayıp ve bozuk veri analizi
import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ['a','c','e','f','h'],columns=  ['column1','column2','column3'])

result = df
df =df.reindex(['a','b','c','d','e','f','g','h'])
result1 = df

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

result2 = df.drop("column1",axis=1) #siler
result3 = df.drop(["column1","column2"], axis = 1)#sütun
result4 = df.drop('a', axis = 0) #satır
result5 = df.drop(['a','b','h'], axis = 0)

print(result)
#   column1  column2  column3
#a       47       96       62
#c       38       71       97
#e       71       16       62
#f       10       46       37
#h       22       23       39
print(result1)
#   column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#b      NaN      NaN      NaN     30.0
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#g      NaN      NaN      NaN      NaN
#h     22.0     23.0     39.0     10.0
print(result2)
# column2  column3  column4
#a     96.0     62.0      NaN
#b      NaN      NaN     30.0
#c     71.0     97.0      NaN
#d      NaN      NaN     51.0
#e     16.0     62.0      NaN
#f     46.0     37.0     30.0
#g      NaN      NaN      NaN
#h     23.0     39.0     10.0
print(result3)
#column3  column4
#a     62.0      NaN
#b      NaN     30.0
#c     97.0      NaN
#d      NaN     51.0
#e     62.0      NaN
#f     37.0     30.0
#g      NaN      NaN
#h     39.0     10.0
print(result4)
# column1  column2  column3  column4
#b      NaN      NaN      NaN     30.0
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#g      NaN      NaN      NaN      NaN
#h     22.0     23.0     39.0     10.0
print(result5)
#  column1  column2  column3  column4
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#g      NaN      NaN      NaN      NaN

print("************************")

result6 = df.isnull() #boş kısımlar True
result7 = df.notnull() #dolu kısımlar True
result8 = df.isnull().sum() #boş kısımların sayısı
result9 = df["column1"].isnull().sum() #ilk sütun boş kısımların sayısı
result10 = df[df["column1"].isnull()] #ilk sütunda NAN degere sahip satırlar hepsi yazar
result11 = df[df["column1"].isnull()]["column1"] #ilk sütundaki nan degere sahip satırlar sadece ilk sütun
result12 = df[df["column1"].notnull()]["column1"] ##ilk sütundaki bir degere sahip satırlar sadece ilk sütun

print(result1)
# column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#b      NaN      NaN      NaN     30.0
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#g      NaN      NaN      NaN      NaN
#h     22.0     23.0     39.0     10.0
print(result6)
# column1  column2  column3  column4
#a    False    False    False     True
#b     True     True     True    False
#c    False    False    False     True
#d     True     True     True    False
#e    False    False    False     True
#f    False    False    False    False
#g     True     True     True     True
#h    False    False    False    False
print(result7)
# column1  column2  column3  column4
#a     True     True     True    False
#b    False    False    False     True
#c     True     True     True    False
#d    False    False    False     True
#e     True     True     True    False
#f     True     True     True     True
#g    False    False    False    False
#h     True     True     True     True
print(result8)
#column1    3
#column2    3
#column3    3
#column4    4
#dtype: int64
print(result9)#3
print(result10)
# column1  column2  column3  column4
#b      NaN      NaN      NaN     30.0
#d      NaN      NaN      NaN     51.0
#g      NaN      NaN      NaN      NaN
print(result11)
#b   NaN
#d   NaN
#g   NaN
#Name: column1, dtype: float64
print(result12)
#a    47.0
#c    38.0
#e    71.0
#f    10.0
#h    22.0
#Name: column1, dtype: float64

print("************************")


result13 = df.dropna()#satırlarda hiç nan değeri olmayan satırları yazdrır   default degeri # axis = 0 => satıra 
result14 = df.dropna(axis = 1) #sütundalarda hiç nan degeri olmayan sütunları yazdrır axis = 1 => sütuna 
result15 = df.dropna(how = "any")
result16 = df.dropna(how = "all") #bütün satır nansa siler bütün sütunlarda arıyor
result17 = df.dropna(subset  = ["column1","column2"], how = "all") #subset => hangi sütunlarda
result18 = df.dropna(subset  = ["column1","column2"], how = "any") #1.ve2.sütunda nan degeri varsa onu yazdırmaz
result19 = df.dropna(thresh = 2)
result20 = df.dropna(thresh = 4) # en az sayıda normal veri

print(result1)
#  column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#b      NaN      NaN      NaN     30.0
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#g      NaN      NaN      NaN      NaN
#h     22.0     23.0     39.0     10.0
print(result13)
#   column1  column2  column3  column4
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result14)
#Empty DataFrame
#Columns: []
#Index: [a, b, c, d, e, f, g, h]
print(result15)
#column1  column2  column3  column4
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result16)
#column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#b      NaN      NaN      NaN     30.0
#c     38.0     71.0     97.0      NaN
#d      NaN      NaN      NaN     51.0
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result17)
#column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#c     38.0     71.0     97.0      NaN
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result18)
#column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#c     38.0     71.0     97.0      NaN
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result19)
# column1  column2  column3  column4
#a     47.0     96.0     62.0      NaN
#c     38.0     71.0     97.0      NaN
#e     71.0     16.0     62.0      NaN
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0
print(result20)
# column1  column2  column3  column4
#f     10.0     46.0     37.0     30.0
#h     22.0     23.0     39.0     10.0

print("************************")

result21 = df.fillna(value="No input") # nan kısımları doldurur.
result22 = df.sum() #sütunlardaki toplamları söyler
result23 = df.sum().sum() #toplam
result24 = df.size #toplam eleman sayisini söyler(nan dahil)
result25 = df.isnull().sum()#sütunlardaki boş elemanların sayısı
result26 = df.isnull().sum().sum()#toplam boş elemanların sayısı
result27 = df.size - df.isnull().sum().sum() #nan hariç eleman sayısı
print(result21)
# column1   column2   column3   column4
#a      47.0      96.0      62.0  No input
#b  No input  No input  No input      30.0
#c      38.0      71.0      97.0  No input
#d  No input  No input  No input      51.0
#e      71.0      16.0      62.0  No input
#f      10.0      46.0      37.0      30.0
#g  No input  No input  No input  No input
#h      22.0      23.0      39.0      10.0
print(result22)
#column1    188.0
#column2    252.0
#column3    297.0
#column4    121.0
#dtype: float64
print(result23)#858.0
print(result24)#32
print(result25)
#column1    3
#column2    3
#column3    3
#column4    4
#dtype: int64
print(result26)#13
print(result27)#19

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet
result28 = df.fillna(value = ortalama(df))
print(ortalama(df))#45.1578947368421
print(result28)
# column1    column2    column3    column4
#a  47.000000  96.000000  62.000000  45.157895
#b  45.157895  45.157895  45.157895  30.000000
#c  38.000000  71.000000  97.000000  45.157895
#d  45.157895  45.157895  45.157895  51.000000
#e  71.000000  16.000000  62.000000  45.157895
#f  10.000000  46.000000  37.000000  30.000000
#g  45.157895  45.157895  45.157895  45.157895
#h  22.000000  23.000000  39.000000  10.000000