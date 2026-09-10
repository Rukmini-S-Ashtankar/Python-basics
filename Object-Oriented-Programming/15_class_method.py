class Student:
    college = "ABC College"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college


print("Before:", Student.college)

Student.change_college("XYZ College")

print("After:", Student.college)
