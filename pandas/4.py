import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns = ["Column1","Column2","Column3"])
result = df
result1 = df["Column1"]
result2 = type(df["Column1"])
result3 = df[["Column1","Column2"]]

#loc["row","column"] => loc["row"] => loc[:,"column"]
result4 = df.loc["A"]
result5 = type(df.loc["A"])

result6 = df.loc[:,"Column1"]
result7= df.loc[:,["Column1","Column2"]]
result8= df.loc[:,"Column1":"Column2"]#column1 ile column2 arasındaki tüm columnları alır ikiside dahil(başlangıc ve bitiş dahil)
#result9= df.loc[:,:"Column2"] başlangıctan al

result9 = df.loc["B":"C","Column2":"Column3"] # BdeCye kadar olan satırları and Column2den Column3e kadar olan columnları al

#result10 = df.loc[0] #hata verir
result11 = df.iloc[0]# A. indesi verir

result12 = df.loc["B","Column2"] #B.index 2.Column nasıl erişebiliriz.
result13 = df.loc[["A","B"],["Column1","Column2"]]

print(result)
#    Column1   Column2   Column3
#A  0.551388  0.665741  0.478601
#B  0.085392  0.291411  0.891352
#C  0.096987  0.365467  0.149504
print(result1)
#A    0.551388
#B    0.085392
#C    0.096987
#Name: Column1, dtype: float64 
print(result2)
#<class 'pandas.core.series.Series'>
print(result3)
#    Column1   Column2
#A  0.551388  0.665741
#B  0.085392  0.291411
#C  0.096987  0.365467
print(result4)
#Column1    0.551388
#Column2    0.665741
#Column3    0.478601
#Name: A, dtype: float64
print(result5)
#<class 'pandas.core.series.Series'>
print(result6)
#A    0.551388
#B    0.085392
#C    0.096987
#Name: Column1, dtype: float64
print(result7)
#    Column1   Column2
#A  0.551388  0.665741
#B  0.085392  0.291411
#C  0.096987  0.365467
print(result8)
#    Column1   Column2
#A  0.551388  0.665741
#B  0.085392  0.291411
#C  0.096987  0.365467
print(result9)
#    Column2   Column3
#B  0.291411  0.891352
#C  0.365467  0.149504
print(result11)
#Column1    0.551388
#Column2    0.665741
#Column3    0.478601
#Name: A, dtype: float64
print(result12)
#0.29141086389453297
print(result13)
#    Column1   Column2
#A  0.551388  0.665741
#B  0.085392  0.291411

print("**********************")

df1 = pd.DataFrame(randn(3,3),index=["A","B","C"],columns = ["Column1","Column2","Column3"])
df1["Column4"] = pd.Series(randn(3),["A","B","C"])
df1["Column5"] = df1["Column1"] + df1["Column3"]

#silmek için df.drop

#df.drop("Column2") # bu hata verir xvey kordinatı belirtilmemiş
print(df1.drop("Column2",axis=1)) #burada yapılan değer için bir güncelleme yapılır.
#    Column1   Column3   Column4   Column5
#A  1.221020  1.024900 -0.585582  2.245921
#B  0.279641 -0.281525  0.001966 -0.001883
#C -0.312644  0.363842  0.215638  0.051198
result14 = df1
print(result14)#original dataframe değişmez
#    Column1   Column2   Column3   Column4   Column5
#A  1.221020 -1.960389  1.024900 -0.585582  2.245921
#B  0.279641 -1.110866 -0.281525  0.001966 -0.001883
#C -0.312644 -0.491806  0.363842  0.215638  0.051198

print("-----------------------------")

df2= pd.DataFrame(randn(3,3),index=["A","B","C"],columns = ["Column1","Column2","Column3"])
df2["Column4"] = pd.Series(randn(3),["A","B","C"])
df2["Column5"] = df2["Column1"] + df2["Column3"]

#silmek için df.drop
#df.drop("Column2") # bu hata verir xvey kordinatı belirtilmemiş
print(df2.drop("Column2",axis=1,inplace=True)) #inplace=True ile dataframe üzerinde de değişiklik yapılır
#None
result15 = df2
print(result15)
#    Column1   Column3   Column4   Column5
#A -0.706109 -1.497574 -0.582182 -2.203683
#B -0.364149 -1.108400 -0.110567 -1.472548
#C -0.800120 -1.681388 -0.413461 -2.481509