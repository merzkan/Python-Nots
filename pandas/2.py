'''
pandas serileri gördük pandas dataframelerini görcez
data DataFrameler=serilerin birleşmiş hali
'''
import pandas as pd

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)
#   apples  oranges
#0       3        0
#1       2        3
#2       0        7
#3       1        2

print("*****************")

df1 = pd.DataFrame()
print(df1)
#Empty DataFrame  
#Columns: []      
#Index: [] 

print("*****************")

df2 = pd.DataFrame([1,2,3,4])
print(df2)
#   0
#0  1
#1  2
#2  3
#3  4

print("*****************")

df3 = pd.DataFrame([["ahmet",50],["ali",60],["yagmur",70],["çınar",80]])
print(df3)
#        0   1
#0   ahmet  50
#1     ali  60
#2  yagmur  70
#3   çınar  80

print("*****************")

data1 = [["ahmet",50],["ali",60],["yagmur",70],["çınar",80]]
df4 = pd.DataFrame(data1, columns= ["Name","Grade"],index=[1,2,3,4])
#df4 = pd.DataFrame(data1,[1,2,3,4],["Name","Grade"]) # sıralı şeklde olursa hata vermez data,index,column
print(df4)
#     Name  Grade
#1   ahmet     50 
#2     ali     60
#3  yagmur     70
#4   çınar     80

print("*****************")

dict = {"Name":["ahmet","ali","yagmur","cınar"],"grade":[50,60,70,80]}
dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"ali","Grade":50},
                {"Name":"yagmur","Grade":50},
                {"Name":"cınar","Grade":50},
            ]
df5 = pd.DataFrame(dict,index=["212","232","236","456"])
df6 = pd.DataFrame(dict_list,index=["212","232","236","456"])
print(df5)
#       Name  grade
#212   ahmet     50
#232     ali     60
#236  yagmur     70
#456   cınar     80
print(df6)
#       Name  Grade
#212   Ahmet     50
#232     ali     50
#236  yagmur     50
#456   cınar     50