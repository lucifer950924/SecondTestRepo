class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
      print(self.name, self.age, self.gender)


class Student(Human):
    def __init__(self,name,age,gender,identity):
        super().__init__(name, age, gender)
        self.identity = identity

    def get_details(self):
        return self.name, self.age, self.gender,self.identity




class School(Student):
    def __init__(self,name,age,gender,identity):
        super().__init__(name,age,gender,identity)


    def _is_eligible_for_college(self):
        if self.age >= 18:
            return True
        else:
            return False



s1 = Student("Arnab",28,"male",100)
a,b,c,d = s1.get_details()

print(f"The Student name is: {a} \n age: {b} \n gender: {c},identity : {d}")
res = School("Arnab",28,"male",100)
if res._is_eligible_for_college() == True:
    print("eligible for college")
else:
    print("not Eligible")

