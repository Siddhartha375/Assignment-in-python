class Employee:
    company="Google"

    def showDetails(self):
        print("This is an employee.") # this is called overriding

class Customer(Employee):
    language='Python'

    def getName(self):
        print(f"The language is={self.language}")

    def showDetails(self):
        print("This is an Customer.")

e=Employee()
e.showDetails()
p=Customer()
p.getName()
e.showDetails()
#print(p.company)              