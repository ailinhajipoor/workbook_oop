# . Vehicles include wagons, bicycles, motor vehicles (motorcycles, cars, trucks, buses),
# railed vehicles (trains, trams), watercraft (ships, boats),
# amphibious vehicles (screw-propelled vehicle, hovercraft),
# aircraft (airplanes, helicopters) and spacecraft

class Vehicle():
    def __init__(self,  Type, Country_name, Name, Model, Price):
        self.Type = Type
        self.Country_name = Country_name
        self.Name = Name
        self.Model = Model
        self.Price = Price

