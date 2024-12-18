#join ve merge
import pandas as pd

customers = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}
orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}
df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

print(df_customers)
#   CustomerId FirstName LastName
#0           1     Ahmet   Yılmaz
#1           2       Ali  Korkmaz
#2           3     Hasan    Çelik
#3           4     Canan   Toprak
print(df_orders)
#   OrderId  CustomerId   OrderDate
#0       10           1  2010-07-04
#1       11           2  2010-08-04
#2       12           5  2010-07-07
#3       13           7  2012-07-04
result = pd.merge(df_customers,df_orders,how="inner")
result1= pd.merge(df_customers,df_orders,how="left")
result2= pd.merge(df_customers,df_orders,how="right")
result3= pd.merge(df_customers,df_orders,how="outer")

print(result)
#   CustomerId FirstName LastName  OrderId   OrderDate
#0           1     Ahmet   Yılmaz       10  2010-07-04
#1           2       Ali  Korkmaz       11  2010-08-04
print(result1)
#   CustomerId FirstName LastName  OrderId   OrderDate
#0           1     Ahmet   Yılmaz     10.0  2010-07-04
#1           2       Ali  Korkmaz     11.0  2010-08-04
#2           3     Hasan    Çelik      NaN         NaN
#3           4     Canan   Toprak      NaN         NaN
print(result2)
#   CustomerId FirstName LastName  OrderId   OrderDate
#0           1     Ahmet   Yılmaz       10  2010-07-04
#1           2       Ali  Korkmaz       11  2010-08-04
#2           5       NaN      NaN       12  2010-07-07
#3           7       NaN      NaN       13  2012-07-04
print(result3)
#   CustomerId FirstName LastName  OrderId   OrderDate
#0           1     Ahmet   Yılmaz     10.0  2010-07-04
#1           2       Ali  Korkmaz     11.0  2010-08-04
#2           3     Hasan    Çelik      NaN         NaN
#3           4     Canan   Toprak      NaN         NaN
#4           5       NaN      NaN     12.0  2010-07-07
#5           7       NaN      NaN     13.0  2012-07-04

print("*****************")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])


result4 = pd.concat([df_customersA,df_customersB])
result5 = pd.concat([df_customersA,df_customersB],axis=1)
print(result4)
#   CustomerId FirstName LastName
#0           1     Ahmet   Yılmaz
#1           2       Ali  Korkmaz
#2           3     Hasan    Çelik
#3           4     Canan   Toprak
#0           4    Yağmur    Bilge
#1           5     Çınar    Turan
#2           6    Cengiz   Yılmaz
#3           7       Can    Turan
print(result5)
#   CustomerId FirstName LastName  CustomerId FirstName LastName
#0           1     Ahmet   Yılmaz           4    Yağmur    Bilge
#1           2       Ali  Korkmaz           5     Çınar    Turan
#2           3     Hasan    Çelik           6    Cengiz   Yılmaz
#3           4     Canan   Toprak           7       Can    Turan