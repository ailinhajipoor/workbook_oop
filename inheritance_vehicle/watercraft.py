from inheritance_vehicle.vehicle import Vehicle


class Watercraft(Vehicle):
    def __init__(self, Type, Country_name, Name, Model, Price, Number_of_passenger, Color, Generation_year):
        Vehicle.__init__(self, Type, Country_name, Name, Model, Price)
        self.Number_of_passenger = Number_of_passenger
        self.Color = Color
        self.Generation_year = Generation_year

    def Ship(self):
        print("Type of vehicle:", self.Type)
        print("Country name:", self.Country_name)
        print("Name:", self.Name)
        print("Model:", self.Model)
        print("Price:", self.Price)
        print("Number of passenger:", self.Number_of_passenger)
        print("Color:", self.Color)
        print("Generation year:", self.Generation_year)

    def Boat(self):
        print("Type of vehicle:", self.Type)
        print("Country name:", self.Country_name)
        print("Name:", self.Name)
        print("Model:", self.Model)
        print("Price:", self.Price)
        print("Number of passenger:", self.Number_of_passenger)
        print("Color:", self.Color)
        print("Generation year:", self.Generation_year)




root = Watercraft("Watercraft", "Germany", "Sachsen", "F219", "10000$", "400", "Green", "2020")
root.Boat()