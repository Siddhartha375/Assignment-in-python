class Employee():
    company="Google"
    salary=100

harry=Employee()
rajni=Employee()
print(harry.company)
print(rajni.company)
#harry.salary=333
#rajni.salary=321
print(harry.salary)
print(rajni.salary)

Employee.company="Amazon" # change the company name by using class name
print(harry.company)
print(rajni.company)