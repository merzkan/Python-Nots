import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost",user="root", password="19762002Aa.",database ="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi")
        print(f"son eklenen kaydin id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="school")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values) # çogul ekleme yapıyoruz.

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayit eklendi")
        print(f"son eklenen kaydin id:{cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")


list=[]
while True:
    name = input("urun adi:")
    price = input("urun fiyati:")
    imageUrl = input("urun resim adi:")
    description = input("urun aciklamasi:")

    list.append((name,price,imageUrl,description))#tuple olarak ekliyoruz

    result = input("devam etmek istiyor musunuz? (Y/N)")
    if result == 'N':
        print("kayitlariniz veritabanina aktariliyor")
        print(list)
        insertProducts(list)
        break
