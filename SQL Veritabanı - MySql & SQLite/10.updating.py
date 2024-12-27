import mysql.connector
from datetime import datetime


def UpdateProduct():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    mycursor = connection.cursor()

    sql = "UPDATE products Set name='Samsung S10', price=5000 where id=5"

    mycursor.execute(sql)

    try:
        connection.commit()
        print(f"{mycursor.rowcount} tane kayit guncellendi.")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandi")

UpdateProduct()
