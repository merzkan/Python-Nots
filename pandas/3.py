'''
pandas ile farklı dosya tiplerinden veri okuma(CSV, Excel, SQL, JSON,database dosyasından)
'''
import sqlite3 #sql_query için  #.db uzantısı
import pandas as pd
df = pd.read
df = pd.read_csv("pandas\\datasets\\sample.csv")
df1 = pd.read_json("pandas\\datasets\\sample.json")
df2 = pd.read_excel("pandas\\datasets\sample.xlsx")
connection = sqlite3.connect("pandas\\datasets\\sample.db")
df3 = pd.read_sql_query("SELECT * FROM students",connection)
print(df)
#year industry_code_ANZSIC  ...    value               unit
#0      2011                    A  ...    46134              COUNT
#1      2011                    A  ...        0              COUNT
#2      2011                    A  ...      279  DOLLARS(millions)
#3      2011                    A  ...     8187  DOLLARS(millions)
#4      2011                    A  ...     8866  DOLLARS(millions)
#...     ...                  ...  ...      ...                ...
#12379  2018                  all  ...   691859  DOLLARS(millions)
#12380  2018                  all  ...   597623  DOLLARS(millions)
#12381  2018                  all  ...    85574  DOLLARS(millions)
#12382  2018                  all  ...  2068648  DOLLARS(millions)
#12383  2018                  all  ...   499274  DOLLARS(millions)
#
#[12384 rows x 7 columns]

print("*****************")

print(df1)
#     Name  Grade 
#0   Ahmet     50 
#1     Ali     60 
#2  Yağmur     70 
#3   Çınar     80 

print("*****************")

print(df2)
#     Name  Grade 
#0     Ali     60 
#1   Ahmet     80 
#2  Yağmur     90 
#3   Yeşim     50 

print("*****************")

print(df3)
#   Id    Name  Grade
#0   1   Ahmet     70
#1   2     Ali     80
#2   3  Yağmur     90

print("*****************")


