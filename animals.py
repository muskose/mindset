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


fido = Dog("Lessi", "kahverengi")
print(fido.color)
fido.yakala()

tekir = Cat("tekir", "alacalı")
print(tekir.name)
print(tekir.color)
tekir.zipla()