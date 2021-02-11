from inheritance_institute.person import Person


class Administer(Person):
    def __init__(self, name, last_name, age, city, phone, gender, marital_status, position):
        super().__init__(name, last_name, age, city, phone)
        self.gender = gender
        self.marital_status = marital_status
        self.position = position

    def display_info(self):
        print(self.position+"'s name is", self.name)
        print(self.position+"'s last name is", self.last_name)
        print(self.position+"'s age is", self.age)
        print(self.position+"'s city is", self.city)
        print(self.position+"'s phone is", self.phone)
        print(self.position+"'s gender is", self.gender)
        print(self.position+"'s marital status is", self.marital_status)


person_info = Administer("Ailin", "Hajipoor", 30, "Rasht", +98911002, "female", "Master of science", "Manager")
person_info.display_info()