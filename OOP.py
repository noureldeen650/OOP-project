class Person:
 def __init__(self,name,age):
     self.n= name
     self.a= age
 def display(self):
  print(f"name:{self.n},age: {self.a}")
class School:
 def __init__(self,name,phonenumber,principalname,TuitFees):
        self.name = name
        self.phoneNumber = phonenumber
        self.principal_name = principalname
        self.tuition_fees =TuitFees
        self.teachers =[]

 students = []
 def getnumberofStudents(self):
      return len(self.students)


 def Class_Size(self):
     return self.class_size

 def register_student(self, student):
  self.students.append(student)
  self.class_size = self.class_size  + 1

 def remove_Student(self,student):
    self.students.pop(student)
    self.class_size = self.class_size - 1

 def costforBUS(self):
    print("Registration for BUS costs 50$")


 def CallFather(self):
    print(f"......Calling the student father {self.fathername}")
class Class(School):


git commit -m "Tic tac game"

class Student(School):
    def __init__(self, name, grade, age, n, fn, pPH, l):
     super().__init__(name, l)
     self.grade = grade
     self.Fname = name
     self.age= age
     self.nationality = n
     self.fathername = fn
     self.parentPhNo = pPH

    def CallFather(self):
        print(f"......Calling the student father with the name {self.name} {self.fathername} ")

    def getinfo(self):
        print(f"the student name:{self.name},age: {self.age},nationality: {self.nationality} ")

class Class:
 students= []
 def addstudent(self,Student):
    self.students.append(Student)
 def Class_Size(self):
        return self
