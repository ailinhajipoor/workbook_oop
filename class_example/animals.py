class Animals():
    def __init__(self, tail, legs, horns):
        self.horns = horns
        self.tail = tail
        self.legs = legs

    def cow(self):
        print("A cow has ", self.tail, " tail.")
        print("A cow has ", self.legs, " legs.")
        print("A cow has ", self.horns, "horn/horns.")

    def horse(self):
        print("A horse has ", self.tail, "tail.")
        print("A horse has ", self.legs, "legs.")
        print("A horse has ", self.horns, "horn/horns.")


MyAnimal = Animals(1, 4, 2)
MyAnimal.cow()

print("-"*30)
YourAnimal=Animals(1,4,0)
MyAnimal.horse()
