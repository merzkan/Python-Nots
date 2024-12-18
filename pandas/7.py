#DataFrame Groupby

import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df
result1 = df["Maaş"].sum()
result2 = df.groupby("Departman").groups
result3 = df.groupby(["Departman","Semt"]).groups
semtler = df.groupby("Semt")
result4 = df.groupby("Semt").get_group("Kadıköy")
result5 = df.groupby("Departman").sum()
result6 = df.groupby("Departman")["Maaş"].mean()
result7 = df.groupby("Semt")["Çalışan"].count()
result8 = df.groupby("Departman")["Yaş"].max()
result9 = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result10 = df.groupby("Departman")[["Yaş","Maaş"]].agg(np.mean)
result11 = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])
result12 = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]

print(result)
print(result1)#29250 maaşlarının toplamı
print(result2)#{'Bilgi İşlem': [1, 4], 'Muhasebe': [2, 5], 'İnsan Kaynakları': [0, 3, 6]}
print(result3)#{('Bilgi İşlem', 'Maltepe'): [4], ('Bilgi İşlem', 'Tuzla'): [1], ('Muhasebe', 'Maltepe'): [2], ('Muhasebe', 'Tuzla'): [5], ('İnsan Kaynakları', 'Kadıköy'): [0, 6], ('İnsan Kaynakları', 'Tuzla'): [3]}
for name,group in semtler:
    print(name)
    print(group)
#Kadıköy
#        Çalışan         Departman  Yaş     Semt  Maaş
#0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
#6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
#Maltepe
#         Çalışan    Departman  Yaş     Semt  Maaş
#2  Hasan Korkmaz     Muhasebe   45  Maltepe  4000
#4      Ali Turan  Bilgi İşlem   23  Maltepe  2750
#Tuzla
#       Çalışan         Departman  Yaş   Semt  Maaş
#1   Can Ertürk       Bilgi İşlem   25  Tuzla  3000
#3  Cenk Saymaz  İnsan Kaynakları   50  Tuzla  3500
#5  Rıza Ertürk          Muhasebe   34  Tuzla  6500
print(result4)
#        Çalışan         Departman  Yaş     Semt  Maaş
#0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
#6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
print(result5)
#                                             Çalışan  Yaş                 Semt   Maaş
#Departman
#Bilgi İşlem                      Can ErtürkAli Turan   48         TuzlaMaltepe   5750
#Muhasebe                    Hasan KorkmazRıza Ertürk   79         MaltepeTuzla  10500
#İnsan Kaynakları  Ahmet YılmazCenk SaymazMustafa Can  122  KadıköyTuzlaKadıköy  13000
print(result6)
#Departman
#Bilgi İşlem         2875.000000
#Muhasebe            5250.000000
#İnsan Kaynakları    4333.333333
#Name: Maaş, dtype: float64
print(result7)
#Semt
#Kadıköy    2
#Maltepe    2
#Tuzla      3
#Name: Çalışan, dtype: int64
print(result8)
#Departman
#Bilgi İşlem         25
#Muhasebe            45
#İnsan Kaynakları    50
#Name: Yaş, dtype: int64
print(result9)#6500
print(result10)
#                        Yaş         Maaş
#Departman
#Bilgi İşlem       24.000000  2875.000000
#Muhasebe          39.500000  5250.000000
#İnsan Kaynakları  40.666667  4333.333333
print(result11)
#                    sum         mean   max   min
#Departman
#Bilgi İşlem        5750  2875.000000  3000  2750
#Muhasebe          10500  5250.000000  6500  4000
#İnsan Kaynakları  13000  4333.333333  5000  3500
print(result12)
#sum     10500.0
#mean     5250.0
#max      6500.0
#min      4000.0
#Name: Muhasebe, dtype: float64