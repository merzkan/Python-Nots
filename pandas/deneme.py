import pandas as pd

df = pd.read_excel("pandas\\datasets\\notlar.xlsx")

result = df[(df["Puan"]>=30) & (df["Puan"]<90)]["Puan"].sort_values().mean()

print(result)