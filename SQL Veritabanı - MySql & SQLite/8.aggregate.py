#hesaplama fonksiyonları
import mysql.connector


def getProductsInfo():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    cursor = connection.cursor()

    #sql = "Select COUNT(*) from Products" #bütün bilgileri say
    #sql = "Select AVG(price) from Products" #ortalaması
    #sql = "Select SUM(price) from Products" #toplar
    #sql = "Select MIN(price) from Products" #min
    #sql = "Select MAX(price) from Products" #max
    sql = "Select Name from Products Where Price = (Select MAX(price) from Products)" #en pahalı ürünün adı
    cursor.execute(sql)

    result = cursor.fetchone()
    print(f"result:{result[0]}")

getProductsInfo()

