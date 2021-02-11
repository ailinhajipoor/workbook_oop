from inheritance_institute.person import Person


class Student(Person):
    def __init__(self, name, last_name, age, city, phone, level, score):
        super().__init__(name, last_name, age, city, phone)
        self.level = level
        self.score = score

    def display_info(self):
        print("Student's name is", self.name)
        print("Student's last name is", self.last_name)
        print("Student's age is", self.age)
        print("Student's city is", self.city)
        print("Student's phone is", self.phone)
        print("Stude,nt's level is", self.level)
        print("Student's score is", self.score)


student_info = Student("Anisa", "Vafadar", 10, "Rasht", +98911002, "term2", 20)
student_info.display_info()