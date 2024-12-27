import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1mypassword",
    database="mydatabase" #mydatabase,node-app
)

print(mydb)


mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase") #database oluşturduk

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
 #   print(x)

#mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))") #table oluşturduk
