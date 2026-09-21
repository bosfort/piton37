class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "їсть")


class Pet:
    def __init__(self, owner):
        self.owner = owner

    def play(self):
        print(self.owner, "грається з твариною", self.name)


class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def bark(self):
        print(self.name, "гавкає")


dog = Dog("Бобік", "Олег")

dog.eat()
dog.play()
dog.bark()