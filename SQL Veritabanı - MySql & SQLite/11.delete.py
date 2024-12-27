import mysql.connector
from datetime import datetime

def deleteProduct():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    mycursor = connection.cursor()

    sql = "DELETE from products where id=6"

    mycursor.execute(sql)

    try:
        connection.commit()
        print(f"{mycursor.rowcount} tane kayit silindi.")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandi")

deleteProduct()

#sql = "DELETE from products where name like '&s7&'" içinde s7 geçen herhangi bir kelimeyi siler