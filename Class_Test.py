class Student:
    def __init__(self,name,identity,age,gender):
        self.name = name
        self.identity = identity
        self.age = age
        self.gender = gender

    def show_details(self):
        print(f"The name of student {self.identity} is {self.name}")

    def is_adult(self):
        if self.age > 18:
            return "adult"
        else:
            return "not adult"

class Specialization(Student):
    def __init__(self,name,identity,age,gender,speciality):
        super().__init__(name,identity,age,gender)
        self.speciality = speciality
    def show_student_details(self):
        print(f"The student name is {self.name},id is {self.identity} and specializes in {self.speciality}")
    def is_age(self):
        if self.age >= 21 and self.gender == "male":
            print(f"Adult {self.gender}")
        elif self.age >= 18 and self.gender == "female":
            print(f"Adult {self.gender}")
        else:
            print("not adult")




#This code is about Inheritance and polymorphism in Python
# Inheritance is when a child class(Specialization) takes the methods of a parent class(Student)
#Polymorphism is when a child class changes the method of a parent class
print('\n')


s2 = Specialization("Rahul",201,27,"male","Engineering")
s2.show_student_details()
s2.is_age()
if __name__ == "__main__":
    print("this is code about inheritance in python")

