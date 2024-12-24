#json module

'''
Python'daki json modülü, JSON (JavaScript Object Notation) formatındaki verilerle çalışmak için kullanılan bir modüldür.
JSON, verileri yapılandırılmış bir biçimde saklamak için yaygın olarak kullanılan, hafif bir veri değişim formatıdır.
Hem insanlar hem de makineler tarafından kolayca okunabilir ve yazılabilir.
Python'da JSON formatı genellikle web API'leri ile iletişim kurarken, veritabanlarında veri depolarken,
konfigürasyon dosyaları veya dış veri kaynaklarından veri alıp gönderirken kullanılır.
'''

import json


person_string = '{"name":"Ali", "languages":["python","C#"]}'
person_dict = {"name": "Ali","languages": ["Python","C#"] }

print(type(person_string))
#<class 'str'>
print(type(person_dict))
#<class 'dict'>

print("*************************************")

#JSON string to Dict
result = json.loads(person_string)
result1 = result["name"]

print(result)
#{'name': 'Ali', 'languages': ['python', 'C#']}
print(type(result))
#<class 'dict'>
print(result1)
#Ali

print("*************************************")

with open("person.json") as f:
    data = json.load(f)
    print(data)
    #{'name': 'Ali', 'languages': ['python', 'C#']}

print("*************************************")
print("*************************************")
person_dict1= {
    "name": "Ali",
    "languages": ["Python","C#"] 
    }

# Dict to JSON string
result2 =json.dumps(person_dict1)

print(result2)
#{"name": "Ali", "languages": ["Python", "C#"]}
print(type(result2))
#<class 'str'>
#print(result2["name"])#string indices must be integers, not 'str' artık ulaşamam çünkü string türünde oldu

print("*************************************")

with open("person1.json","w") as f:
    json.dump(person_dict1,f)#dosyamıza ekledik

print("*************************************")
print("*************************************")
person_string2 = '{"name":"Ali", "languages":["python","C#"]}'
person_dict2 = {"name": "Ali","languages": ["Python","C#"] }

person_dict2 = json.loads(person_string2)
print(person_dict2)
#{'name': 'Ali', 'languages': ['python', 'C#']}
result3 = json.dumps(person_dict2, indent=4, sort_keys=True)
print(result3)
#{
#    "languages": [
#        "python",
#        "C#"
#    ],
#    "name": "Ali"
#}