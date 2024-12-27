# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

import mysql.connector

connecton = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mypassword",
    database = "schooldb"
    
)

mycursor = connecton.cursor()

