class Employee:
    company="Google"
    salary=100

    #def changeSalary(self,sal):
     #   self.__class__.salary=sal # change the main method value
        #OR
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(200)
print(e.salary)
print(Employee.salary)