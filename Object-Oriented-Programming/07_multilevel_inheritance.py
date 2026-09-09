class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Puppy(Dog):
    def play(self):
        print("Playing")


puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.play()
