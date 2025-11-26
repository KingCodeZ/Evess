class Profile:

    def __init__(self, name, gender, MatNum, department, Level, session):
        self.name = name
        self.gender = gender
        self.MatNum = MatNum
        self.department = department
        self.Level = Level
        self.session = session


# Collecting User Input
name = input("Enter your name: ")
gender = input("Enter your gender: ")
MatNum = input("Enter your Matriculation Number: ")
department = input("Enter your department: ")
Level = input("Enter your level: ")
session = input("What session did you get admitted: ")

# Creating Object
# Student = Profile(name, gender, MatNum, department, Level, session)
def details(self):
    print("Registration Sucessful!")
    print("------------------Student Information------------------")
    print("Name : {}".format(self.name))
    print("Gender : {}".format(self.gender))
    print("Matriculation Number : {}".format(self.MatNum))
    print("Department : {}".format(self.department))
    print("Level : {}".format(self.Level))
    print("Session : {}".format(self.session))

# inheritance

class StudentProfile(Profile):
    def __init__(self, name, gender, MatNum, department, Level, session, cgpa, phone_number):
        Profile.__init__(self, name, gender, MatNum, department, Level, session)
        self.cgpa = cgpa
        self.phone_number = phone_number


        #polymorphism
    def details(self):
        print("Registration Sucessful!")
        print("------------------Student Information------------------")
        print(">>Your name is {}".format(self.name))
        print(">>A {} Student".format(self.gender))
        print(">>You've been given the matric number of {}".format(self.MatNum))
        print(">>Your department is {}".format(self.department))
        print(">>A {} Level student".format(self.Level))
        print(">>You've been admitted in the {} session".format(self.session))
        print(">>Your current cgpa is {}".format(self.cgpa))
        print(">>Phone Number : {}".format(self.phone_number))

cgpa = input("Enter your current CGPA: ")
phone_number = input("Enter your phone number: ")

student1 = StudentProfile(name, gender, MatNum, department, Level, session, cgpa, phone_number)
student1.details()


















# print("Welcome to our student registration portal.")
# class Profile:

#     def __init__(self):
#         self.Name = input("Enter your name: ")
#         self.gender = input("Enter your gender: ")
#         self.MatNum  = input("Enter your Matriculation Number: ")
#         self.department = input("Enter your department: ")
#         self.Level = input("Enter your level: ")
#         self.session = input("What session did you get admitted: ")
        
# Student = Profile()




# print("Congratulations, your profile has been created. These are your details below:")

# print("------------------Student Information------------------")
# print("Name : {}".format(Student.Name))
# print("Gender : {}".format(Student.gender))
# print("Matriculation Number : {}".format(Student.MatNum))
# print("Department : {}".format(Student.department))
# print("Level : {}".format(Student.Level))
# print("Session : {}".format(Student.session))
