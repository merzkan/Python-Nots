#   a- Tüm öğrenci kayıtlarını alınız.
    #  sql = "SELECT * from student"

#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
    #  sql = "SELECT studentnumber,name,surname from student"

#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
    #  sql = "SELECT name,surname from student where gender='K'"

#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
    #  sql = "SELECT * from student where YEAR(birthdate)=2003"

#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
    #  sql = "SELECT * from student where name='ali' and YEAR(birthdate)=2005"

#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
    #  sql = "SELECT * from student where name like '%an%' or surname like '%an%'"

#   g- Kaç erkek öğrenci vardır ?
    #  sql = "select COUNT(*) from student where gender='E'"

#   h- Kız öğrencileri harf sırasına göre getiriniz.
    #  sql = "SELECT * from student where gender='K' ORDER BY name,surname"

#sql = "select * from student LIMIT 5" # ilk 5 kayıt gelir.

import mysql.connector
from datetime import datetime


def StudentInfo():
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="schooldb")
    mycursor = connection.cursor()

    sql = "SELECT * from student where gender='K' ORDER BY name,surname"

    mycursor.execute(sql)
    try:
        results = mycursor.fetchall()
        for result in results:
            print(result)
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
    
StudentInfo()

