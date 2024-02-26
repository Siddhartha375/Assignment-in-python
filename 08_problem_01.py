class programmer:
    company="Microsoft"
    def __init__(self, name, product) :
        self.name=name
        self.product=product

    def getInfo(self):
            print(f"The name of the programmer is {self.name} and the product is {self.product}")
harry=programmer("Harry","Skype")       
alka=programmer("Alka","Github")
harry.getInfo()
alka.getInfo()