from inheritance_institute.person import Person


class Teacher(Person):
    def __init__(self, name, last_name, age, city, phone, universityDegree, Nationality):
        super().__init__(name, last_name, age, city, phone)
        self.universityDegree = universityDegree
        self. Nationality = Nationality

    def display_info(self):
        print("Teacher's name is", self.name)
        print("Teacher's last name is", self.last_name)
        print("Teacher's age is", self.age)
        print("Teacher's city is", self.city)
        print("Teacher's phone is", self.phone)
        print("Teacher's university degree is", self.universityDegree)
        print("Teacher's nationality is", self.Nationality)


teacher_info = Teacher("Niloufar", "Rahimizadeh", 27, "Rasht", +98911002, "Master of science", "Iranian")
teacher_info.display_info()