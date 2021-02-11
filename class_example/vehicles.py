class Vehicle ():
    def __init__(self,doors,company,color,wheels):
        self.doors=doors
        self.company=company
        self.color=color
        self.wheels=wheels
    def MyCar(self):
        print("my car has " ,self.doors," doors")
        print("my car has " ,self.wheels," wheels")
        print("my car is " ,self.color)
        print("my car is belong to ",self.company)

x530=Vehicle(4,"MVM","black",4)
x530.MyCar()