#DataFrame Metotları
import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}
df = pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2 = lambda x: x*x

result = df
result1 = df["Column2"].unique() #aynı elemandan birden çok varsa 1 taneisni yaz
result2 = df["Column2"].nunique() # 4 tane tekil sayı var.(2 tane 20 oldugu için 1 tane 20 sayar)
result3 = df["Column2"].value_counts() # degerlerı kac defa tekrarlaıgını
result4 = df["Column1"]*2
result5 = df["Column1"].apply(kareal)
result6 = df["Column1"].apply(kareal2)
result7 = df["Column1"].apply(lambda x: x*x)
df["Column4"] = df["Column3"].apply(len)

print(result)
#   Column1  Column2 Column3
#0        1       10     abc
#1        2       20    bcaa
#2        3       13     ade
#3        4       20      cb
#4        5       25     dea
print(result1)#[10 20 13 25]
print(result2)#4
print(result3)
#Column2      
#20    2
#10    1
#13    1
#25    1
#Name: count, dtype: int64
print(result4)
#0     2
#1     4
#2     6
#3     8
#4    10
#Name: Column1, dtype: int64
print(result5)
#0     1
#1     4
#2     9
#3    16
#4    25
#Name: Column1, dtype: int64
print(result6)
#0     1
#1     4
#2     9
#3    16
#4    25
#Name: Column1, dtype: int64
print(result7)
#0     1
#1     4
#2     9
#3    16
#4    25
#Name: Column1, dtype: int64
print(df)
#   Column1  Column2 Column3  Column4
#0        1       10     abc        3
#1        2       20    bcaa        4
#2        3       13     ade        3
#3        4       20      cb        2
#4        5       25     dea        3


print("*****************")
print("*****************")

data1 = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df1 = pd.DataFrame(data1)

result8 = df1.columns# isimlerini öğrenmek için
result9 = len(df1.columns) #sayısını
result10 = df.index # index bilgileri
result11 = len(df.index) # index sayısı
result12 = df.info

result13 = df.sort_values("Column2") #sıralı sıralanır
result14 = df.sort_values("Column3") #alfabetik
result15 = df.sort_values
result16 = df.sort_values("Column3",ascending=False)#azalan bir şekilde



print(result8)#Index(['Column1', 'Column2', 'Column3'], dtype='object')
print(result9)#3
print(result10)#RangeIndex(start=0, stop=5, step=1)
print(result11)#5
print(result12)
#<bound method DataFrame.info of    Column1  Column2 Column3  Column4
#0        1       10     abc        3
#1        2       20    bcaa        4
#2        3       13     ade        3
#3        4       20      cb        2
#4        5       25     dea        3>
print(result13)
#   Column1  Column2 Column3  Column4
#0        1       10     abc        3
#2        3       13     ade        3
#1        2       20    bcaa        4
#3        4       20      cb        2
#4        5       25     dea        3
print(result14)
#   Column1  Column2 Column3  Column4
#0        1       10     abc        3
#2        3       13     ade        3
#1        2       20    bcaa        4
#3        4       20      cb        2
#4        5       25     dea        3
print(result15)
#<bound method DataFrame.sort_values of    Column1  Column2 Column3  Column4   
#0        1       10     abc        3
#1        2       20    bcaa        4
#2        3       13     ade        3
#3        4       20      cb        2
#4        5       25     dea        3>
print(result16)
#   Column1  Column2 Column3  Column4
#4        5       25     dea        3
#3        4       20      cb        2
#1        2       20    bcaa        4
#2        3       13     ade        3
#0        1       10     abc        3

print("********************")

data2 = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data2)

result17 = df
result18 = df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

print(result17)
#        Ay    Kategori  Gelir
#0    Mayıs  Elektronik     20
#1  Haziran  Elektronik     30
#2    Nisan  Elektronik     15
#3    Mayıs       Kitap     14
#4  Haziran       Kitap     32
#5    Nisan       Kitap     42
#6    Mayıs       Giyim     12
#7  Haziran       Giyim     36
#8    Nisan       Giyim     52
print(result18)
#Kategori  Elektronik  Giyim  Kitap
#Ay
#Haziran         30.0   36.0   32.0
#Mayıs           20.0   12.0   14.0
#Nisan           15.0   52.0   42.0