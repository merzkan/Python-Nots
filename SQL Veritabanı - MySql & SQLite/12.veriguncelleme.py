#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.


#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import mysql.connector
from datetime import datetime

class Student:
    connection = mysql.connector.connect(host="localhost",user="root", password="mypassword",database ="schooldb")
    mycursor = connection.cursor()
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("hata",err)

    def updateStudent(self):
        sql = "UPDATE student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit güncellendi")
        except mysql.connector.Error as err:
            print("hata",err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)
        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("hata",err)

    @staticmethod
    def updateStudents(liste):
        sql = "UPDATE student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayit güncellendi")
        except mysql.connector.Error as err:
            print("hata",err)


#student = Student.getStudentById(12)

#student.name = "Çınar"
#student.surname = "Turan"
#student.updateStudent()


students = Student.getStudentsGender("E")
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = "Mr " + std[2]
    liste.append(std)

Student.updateStudents(liste)