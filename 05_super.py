class Person:
    company="Google"
    def __init__(self):
        super().__init__()
        print(" I am Person.")
    def disp(self):
        print("I am Siddhartha")

class Employee(Person):
    company="Youtube"
    def __init__(self):
        super().__init__()
        print("I am employee class.")
    def show(self):
        print("I am Harry")

class Programmer(Employee) :
    def __init__(self):
        super().__init__()
        print("I am Programmer ")

    def details(self):
        print("I am not a programmer ")

#p=Person()
#e=Employee()
pr=Programmer()
                       