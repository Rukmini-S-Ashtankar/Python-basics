
import json

with open("students.json", "r") as file:
    student = json.load(file)

print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])
