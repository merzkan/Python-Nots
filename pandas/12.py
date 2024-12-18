#Nba verileri
import pandas as pd

df = pd.read_csv("pandas\\datasets\\nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(df.index)  # 458

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
#print(df.columns)Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight','College', 'Salary'],dtype='object')
result = df["Salary"].mean() #4842684.105381166

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max() #25000000.0

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0] #Kobe Bryant

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"]<25) & (df["Age"]>=20)][["Name","Team","Age"]].sort_values("Age",ascending=False)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = df.groupby("Team").mean(numeric_only=True)["Salary"]

# 9- Kaç farklı takım mevcut ? #30
#df.dropna(inplace=True) #benim yöntem
#result = len(df["Team"].unique()) #benim yöntem

#result = len(df.groupby("Team"))

#result = df["Team"].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır ?

result = df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace=True)
#result = df[df["Name"].str.contains("and")]

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]


print(result)