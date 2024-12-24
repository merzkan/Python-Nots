import requests
import json
api_key = ""
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan doviz turu:")#USD,TRY
alinan_doviz = input("alinan doviz turu:")#TRY
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:"))

sonuc = requests.get(api_url + bozulan_doviz)
data = json.loads(sonuc.text)
#sonucu verir
#print(data["conversion_rates"][alinan_doviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,data["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*data["conversion_rates"][alinan_doviz],alinan_doviz))
