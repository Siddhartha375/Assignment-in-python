class Employee:
    company="Google"
    def disp(self):
        print("I am parent class no 1")

class Programmer:
    company="Youtube"
    def show(self):
        print("I am also parent class no 2") 

class Child(Employee,Programmer): # ekhane Employee 1st a6e bole tar priority age
    name="Rohit"
    def showname(self):
        print("My name is Rohit Sharma")

obj=Employee()
obj2=Programmer()
obj3=Child()
obj3.disp()
obj3.showname()
print(obj3.company)

print(obj2.company)                     