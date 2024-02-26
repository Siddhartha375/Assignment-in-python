class Calculator:
    def __init__(self, num):
        self.number=num

    def square(self):
        print(f"The square of the {self.number} is {self.number**2}")
    def cube(self):
        print(f"The cube of the {self.number} is {self.number**3}")

    @staticmethod
    def greet():
        print("Welcome to our new page") 

a=Calculator(4)
a.square()
a.cube()
a.greet()
