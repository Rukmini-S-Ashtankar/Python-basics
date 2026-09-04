class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


student = Student("Rukmini")
student.introduce()
