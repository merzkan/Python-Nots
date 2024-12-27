import mysql.connector


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By price") #fyata göre sıralama

    result = cursor.fetchall()

    for product in result:
        print(f"id: {product[0]} name:{product[1]} price: {product[2]}")

getProducts()

#cursor.execute("Select * From Products Order By price DESC") # azalan sırada
#cursor.execute("Select * From Products Order By  name,price") #önce name sıralar sonra price
