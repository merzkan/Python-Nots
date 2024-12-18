#DataFrame Filtreleme
import pandas as pd
import numpy as np


data = np.random.randint(10,100,75).reshape(15,5)#rastegele 10ile 100 arasında 75 tane sayi 15 satır 5sütunluk bir seri tanımlarız.
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5",])

result = df
result1 = df.columns
result2 = df.head() #ilk 5 tane
result3 = df.head(10) #ilk 10tanesi 
result4 = df.tail() #son 5
result5 = df.tail(10) #son 10 kayıt
result6 = df["Column1"].head() #1.sütundaki ilk 5 veriyi
result7 = df.Column1.head() #üsttekinin aynısı
result8 = df[["Column1","Column2"]].head() #1.ve2.satırdaki ilk 5  
result9 = df[["Column1","Column2"]].tail()
result10 = df[5:15][["Column1","Column2"]].head()#5ile15 arasında ilk 5
result11 = df[5:15][["Column1","Column2"]].tail()#5ile15 arasında son5
 

print(result)
#  Column1  Column2  Column3  Column4  Column5
#0        93       61       65       98       72
#1        56       14       40       81       38
#2        14       66       50       75       89
#3        47       31       22       20       75
#4        99       50       71       80       59
#5        30       77       89       49       47
#6        67       21       98       19       80
#7        91       71       60       78       28
#8        64       51       62       66       50
#9        26       66       65       76       26
#10       16       46       23       32       44
#11       82       85       35       97       33
#12       70       51       49       47       22
#13       80       71       44       96       69
#14       32       93       96       15       41
print(result1)
#Index(['Column1', 'Column2', 'Column3', 'Column4', 'Column5'], dtype='object')
print(result2)
#  Column1  Column2  Column3  Column4  Column5
#0       93       61       65       98       72
#1       56       14       40       81       38
#2       14       66       50       75       89
#3       47       31       22       20       75
#4       99       50       71       80       59
print(result3)
#  Column1  Column2  Column3  Column4  Column5
#0       93       61       65       98       72
#1       56       14       40       81       38
#2       14       66       50       75       89
#3       47       31       22       20       75
#4       99       50       71       80       59
#5       30       77       89       49       47
#6       67       21       98       19       80
#7       91       71       60       78       28
#8       64       51       62       66       50
#9       26       66       65       76       26
print(result4)
# Column1  Column2  Column3  Column4  Column5
#10       16       46       23       32       44
#11       82       85       35       97       33
#12       70       51       49       47       22
#13       80       71       44       96       69
#14       32       93       96       15       41
print(result5)
#  Column1  Column2  Column3  Column4  Column5
#5        30       77       89       49       47
#6        67       21       98       19       80
#7        91       71       60       78       28
#8        64       51       62       66       50
#9        26       66       65       76       26
#10       16       46       23       32       44
#11       82       85       35       97       33
#12       70       51       49       47       22
#13       80       71       44       96       69
#14       32       93       96       15       41
print(result6)
#0    93
#1    56
#2    14
#3    47
#4    99
#Name: Column1, dtype: int32
print(result7)
#0    93
#1    56
#2    14
#3    47
#4    99
#Name: Column1, dtype: int32
print(result8)
#  Column1  Column2
#0       93       61
#1       56       14
#2       14       66
#3       47       31
#4       99       50
print(result9)
#Column1  Column2
#10       16       46
#11       82       85
#12       70       51
#13       80       71
#14       32       93
print(result10)
#Column1  Column2
#5       30       77
#6       67       21
#7       91       71
#8       64       51
#9       26       66
print(result11)
# Column1  Column2
#10       16       46
#11       82       85
#12       70       51
#13       80       71
#14       32       93

print("****************")
print("****************")

data1 = np.random.randint(10,100,75).reshape(15,5)

df1 = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5",])
result12 = df1 > 50
result13 = df1[result12]
result14 = df1[df % 2==0]
result15 = df1["Column1"] > 50
result16 = df1[df1["Column1"] > 50]
result17 = df1[df1["Column1"] > 50][["Column1","Column2"]]
result18 = df1[(df1["Column2"] >50) & (df1["Column1"] <=70)]
result19 = df1.query("Column1>=50 & Column1 % 2 == 0")
result20 = df1.query("Column1>=50 & Column1 % 2 == 0")[["Column1","Column2"]]
print(df1)
#    Column1  Column2  Column3  Column4  Column5
#0        63       42       84       84       75
#1        30       74       42       73       90
#2        61       50       47       17       61
#3        83       43       76       79       42
#4        99       86       43       37       10
#5        28       72       65       95       54
#6        35       45       28       16       87
#7        91       91       75       38       32
#8        81       85       23       63       93
#9        19       69       18       93       82
#10       22       12       97       32       75
#11       56       60       15       32       12
#12       39       79       37       32       58
#13       64       19       28       78       82
#14       99       49       21       20       39
print(result12)
#    Column1  Column2  Column3  Column4  Column5
#0      True    False     True     True     True
#1     False     True    False     True     True
#2      True    False    False    False     True
#3      True    False     True     True    False
#4      True     True    False    False    False
#5     False     True     True     True     True
#6     False    False    False    False     True
#7      True     True     True    False    False
#8      True     True    False     True     True
#9     False     True    False     True     True
#10    False    False     True    False     True
#11     True     True    False    False    False
#12    False     True    False    False     True
#13     True    False    False     True     True
#14     True    False    False    False    False
print(result13)
#    Column1  Column2  Column3  Column4  Column5
#0      63.0      NaN     84.0     84.0     75.0
#1       NaN     74.0      NaN     73.0     90.0
#2      61.0      NaN      NaN      NaN     61.0
#3      83.0      NaN     76.0     79.0      NaN
#4      99.0     86.0      NaN      NaN      NaN
#5       NaN     72.0     65.0     95.0     54.0
#6       NaN      NaN      NaN      NaN     87.0
#7      91.0     91.0     75.0      NaN      NaN
#8      81.0     85.0      NaN     63.0     93.0
#9       NaN     69.0      NaN     93.0     82.0
#10      NaN      NaN     97.0      NaN     75.0
#11     56.0     60.0      NaN      NaN      NaN
#12      NaN     79.0      NaN      NaN     58.0
#13     64.0      NaN      NaN     78.0     82.0
#14     99.0      NaN      NaN      NaN      NaN
print(result14)
#      Column1  Column2  Column3  Column4  Column5
#0       NaN     42.0     84.0     84.0      NaN
#1      30.0     74.0     42.0      NaN     90.0
#2       NaN     50.0      NaN      NaN      NaN
#3       NaN      NaN     76.0      NaN     42.0
#4       NaN     86.0      NaN      NaN     10.0
#5      28.0     72.0      NaN      NaN     54.0
#6       NaN      NaN     28.0     16.0      NaN
#7       NaN      NaN      NaN     38.0     32.0
#8       NaN      NaN      NaN      NaN      NaN
#9       NaN      NaN     18.0      NaN     82.0
#10     22.0     12.0      NaN     32.0      NaN
#11     56.0     60.0      NaN     32.0     12.0
#12      NaN      NaN      NaN     32.0     58.0
#13     64.0      NaN     28.0     78.0     82.0
#14      NaN      NaN      NaN     20.0      NaN
print(result15)
#0      True
#1     False
#2      True
#3      True
#4      True
#5     False
#6     False
#7      True
#8      True
#9     False
#10    False
#11     True
#12    False
#13     True
#14     True
#Name: Column1, dtype: bool
print(result16)
#       Column1  Column2  Column3  Column4  Column5
#0        63       42       84       84       75
#2        61       50       47       17       61
#3        83       43       76       79       42
#4        99       86       43       37       10
#7        91       91       75       38       32
#8        81       85       23       63       93
#11       56       60       15       32       12
#13       64       19       28       78       82
#14       99       49       21       20       39
print(result17)
#       Column1  Column2
#0        63       42
#2        61       50
#3        83       43
#4        99       86
#7        91       91
#8        81       85
#11       56       60
#13       64       19
#14       99       49
print(result18)
#       Column1  Column2  Column3  Column4  Column5
#1        30       74       42       73       90
#5        28       72       65       95       54
#9        19       69       18       93       82
#11       56       60       15       32       12
#12       39       79       37       32       58
print(result19)
#      Column1  Column2  Column3  Column4  Column5
#11       56       60       15       32       12
#13       64       19       28       78       82
print(result20)
#       Column1  Column2
#11       56       60
#13       64       19