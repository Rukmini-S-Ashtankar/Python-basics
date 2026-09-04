class Student:
    college = "RBU"

    def __init__(self, name):
        self.name = name


student1 = Student("Rukmini")
student2 = Student("Abhi")

print(student1.name, "-", student1.college)
print(student2.name, "-", student2.college)
