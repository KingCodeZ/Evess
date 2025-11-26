class Student_Registration_Form:
    def __init__(self):
        self.name = input("What is your name: ")
        self.gender = input("What is your gender: ")
        self.matN = input("What is your matriculation number: ")
        self.dept = input("What is your department: ")
        self.level = input("What is your level: ")

student = Student_Registration_Form()

print("The name of the student is {}".format(student.name))
print("The gender of the student is {}".format(student.gender))
print("The matriculation number of the student is {}".format(student.matN))
print("The department of the student is {}".format(student.dept))
print("The level of the student is {}".format(student.level))
