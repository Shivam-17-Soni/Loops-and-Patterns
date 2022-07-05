class Animals:
    animalType="Pet Animals"
    category="Mammal"

class Pets(Animals):
    color="White"

class Dog(Pets):
    @staticmethod
    def bark():
        print(f"Bow bow")

d=Dog()
d.bark()
print(f"{d.animalType}\n{d.color}\n{d.category}")