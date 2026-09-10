class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Buddy", "Labrador")

print("Name:", dog.name)
print("Breed:", dog.breed)
