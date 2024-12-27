'''birden fazla tablo ile çalışma
one to many
many to many

alter table products
add constraint fk_categories_products
foreign key (categoryid) REFERENCES categories(id)
'''
#birden fazla tablodan kayıt seçme
#sql = "Select * from Products inner join Categories on Categories.id=Products.Categoryid"
import mysql.connector


def getProducts():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="node-app")
    cursor = connection.cursor()

    sql = "Select * from Products inner join Categories on Categories.id=Products.Categoryid"

    cursor.execute(sql)

    try:
        results = cursor.fetchall()
        for result in results:
            print(result)
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database baglantisi kapandi")
    
getProducts()