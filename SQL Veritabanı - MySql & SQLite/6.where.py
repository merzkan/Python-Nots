import mysql.connector


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    cursor = connection.cursor()

    #cursor.execute("Select * From Products Where name='Samsung S8' and price=3000 ") #name samsung s8 ve fiyatı 3000 olanlar gelir
    cursor.execute("Select * From Products Where name LIKE '%Samsung%'") #samsung araması yapar. içinde samsung geçen
    result = cursor.fetchall()
    for product in result:
        print(f"id: {product[0]} name:{product[1]} price: {product[2]}")

getProducts()


#cursor.execute("Select * From Products Where name='Samsung S8' and price>3000 ")
#cursor.execute("Select * From Products Where name='Samsung S8' or price=3000 ")
#cursor.execute("Select * From Products Where name LIKE '%Samsung%'")
#cursor.execute("Select * From Products Where name LIKE 'Samsung%'") # en başı samsung sonu ne olursa olsun
#cursor.execute("Select * From Products Where name LIKE '%Samsung'") # sonu samsungla bitecek
