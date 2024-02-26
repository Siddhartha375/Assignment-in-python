class Train:
    def __init__(self,name,price,seats):
        self.name=name
        self.price=price
        self.seats=seats

    def getInfo(self):
        print("*************")
        print(f"The name of the train is={self.name}")
        print(f"The price of the ticket is Rs {self.price}")
        print(f"The available seats in the train is {self.seats}")
        print("*****************")
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket is booked!\n and your seat number is {self.seats}")
            self.seats=self.seats-1 
        else:
            print("Sorry! No tickit are availabale at the time \n Thank you!")

Intercity=Train("Intercity Express:23134",300,1)
Intercity.getInfo()
Intercity.bookTicket()
Intercity.bookTicket()
Intercity.getInfo()