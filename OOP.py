class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class School:
    def __init__(self, name, phone_number, principal_name, tuition_fees):
        self.name = name
        self.phone_number = phone_number
        self.principal_name = principal_name
        self.tuition_fees = tuition_fees
        self.teachers = []
        self.students = []

    def get_number_of_students(self):
        return len(self.students)

    def register_student(self, student):
        self.students.append(student)

    def remove_student(self, student_name):
        self.students = [student for student in self.students if student.name != student_name]

    def cost_for_bus(self):
        print("Registration for BUS costs $50")

    def call_father(self, student_name):
        student = next((s for s in self.students if s.name == student_name), None)
        if student:
            print(f"......Calling the student father {student.father_name}")
        else:
            print(f"Student with name {student_name} not found")

class Student(Person):
    def __init__(self, name, age, grade, nationality, father_name, parent_phone_number):
        super().__init__(name, age)
        self.grade = grade
        self.nationality = nationality
        self.father_name = father_name
        self.parent_phone_number = parent_phone_number

    def call_father(self):
        print(f"......Calling the student father with the name {self.father_name}")

    def get_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Nationality: {self.nationality}, Grade: {self.grade}")

class Class:
    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_size(self):
        return len(self.students)

    def display_info(self):
        print(f"Class: {self.class_name}")
        self.teacher.display()
        print('Students:')
        for student in self.students:
            student.get_info()



school = School("Greenwood High School", "123-456-7890", "Mr. Adams", 10000)


teacher = Person("Mr. Smith", 40)


math_class = Class("Math 101", teacher)
student1 = Student("Alice", 14, "9th Grade", "American", "John Doe", "555-1234")
student2 = Student("Bob", 15, "10th Grade", "British", "David Smith", "555-5678")

math_class.add_student(student1)
math_class.add_student(student2)


school.teachers.append(teacher)
school.register_student(student1)
school.register_student(student2)


school.call_father("Alice")
school.cost_for_bus()
print(f"Number of students in school: {school.get_number_of_students()}")
math_class.display_info()
