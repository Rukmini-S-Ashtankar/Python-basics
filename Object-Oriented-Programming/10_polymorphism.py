class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


for animal in [Dog(), Cat()]:
    animal.sound()
