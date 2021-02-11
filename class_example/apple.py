class Apple():
    def __init__(self, color, taste, size):
        self.color = color
        self.taste = taste
        self.size = size

    def apple(self):
        print("This apple is", self.color, ".")
        print("This apple is", self.taste, ".")
        print("This apple is", self.size, ".")


redApple = Apple("red", "sweet", "big")
redApple.apple()
print(redApple.color)
print(redApple.taste)
print(redApple.size)