class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def zipla(self):
        print("Hoplayı ver kedicik...")

class Dog(Animal):
    def yakala(self):
        print("Yakala Co!")

class Tiger(Cat):
    def avlan(self):
        print("Ceylanı yakala")


shere_khan = Tiger("Shere Khan", "tiger pattern")
print(shere_khan.color)
shere_khan.zipla()
shere_khan.avlan()
