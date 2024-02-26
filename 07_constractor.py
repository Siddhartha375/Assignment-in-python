class Employee:
    company="Google"

    def __init__(self) :
        print("This is run automaticaly") # Always run 

    def __init__(self , salary , subunit):
        self.salary=salary
        self.subunit=subunit
        print("The Employee table is created:") 

    def getDatials(self):
        print(f"The salary= {self.salary}")
        print(f"The subunit is== {self.subunit}")

#harry=Employee()
harry=Employee(123, "Youtube")
harry.getDatials()