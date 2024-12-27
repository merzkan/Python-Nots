import mysql.connector
from datetime import datetime
from Connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id=%s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:",err)

    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class "
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error:",err)        

    def getStudentByClassId(self,classid):
        sql = "select * from student where classid=%s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error:",err)

    def addOrEditStudent(self,student:Student):
        pass

    def addStudent(self, student:Student):#bu yöntemin Student sınıfından türetilmiş bir nesneyi beklediğini ifade eder.
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def editStudent(self, student:Student):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)  

    def addTeacher(self, teacher:Teacher):
        pass

    def editTeacher(self, teacher:Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi")


#db = DbManager()
# student = db.getStudentById(26)
# print(student.name)
# print(student.surname)
#******************************************************
# students = db.getStudentByClassId(1)
# print(students)
#******************************************************
# student = db.getStudentById(26)
# print(student[0].name)
# print(student[0].surname)
#******************************************************
# students = db.getStudentByClassId(1)
# print(students[0].name)

#******************************************************
# db = DbManager()
# student = db.getStudentById(38)
# student[0].name ="Çınar"
# student[0].surname ="turan"
# student[0].studentNumber = "501"

# db.addStudent(student[0])
#******************************************************
# db = DbManager()
# student = db.getStudentById(34)
# student[0].name ="ahmet"
# db.editStudent(student[0])