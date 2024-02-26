class Customer:
    company="Google"
    def disp(self):
        print("I am Customer class.")

    def takebreath(slef):
        print("Your salary is=1200")

class Programmer(Customer):
    company="Amazon" 
    def show(self):
        print("I am Programmer class.")

    def takebreath(self):
        super().takebreath()   # This is the use of Super() keyword.
        print("I am breathing....")

class Employee(Programmer):
    #company="Youtube"
    def output(self):
        print(" I am Employee class .")


c=Customer() 
p=Programmer()
e=Employee()
e.output()
p.takebreath()
e.show()   
print(p.company)
print(e.company)               
