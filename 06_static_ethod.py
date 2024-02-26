class Employee():
    company="Google"
    def getSal(self, signature):
        #print("Salary is 20k")
        print(f"you company is={self.company}\n and salary is {self.Sal}\n {signature}")
@staticmethod
def greet():
    print("Good morning!")
@staticmethod
def time():
    print("The time is 9 AM")

harry =Employee()
harry.Sal=10202
harry.getSal("Thanks")
harry.greet()
harry.time()