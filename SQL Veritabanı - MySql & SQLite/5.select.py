import mysql.connector


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    cursor = connection.cursor()

    #cursor.execute("Select * From Products") #bütün kolonlar
    cursor.execute("Select name,price From Products")
    result = cursor.fetchall() #buldugu bütün kolonları getirir
    #result = cursor.fetchone() #buldugu ilk kaydı getirir
    
    for product in result:
        #print(f"name:{product[1]} price: {product[2]}")
        print(f"name:{product[0]} price: {product[1]}")
getProducts()