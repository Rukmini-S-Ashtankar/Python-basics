
import json

students = [
    {"name": "Rukmini", "marks": 92},
    {"name": "Abhi", "marks": 89},
    {"name": "Tanu", "marks": 78}
]

with open("students_list.json", "w") as file:
    json.dump(students, file, indent=4)

search_name = input("Enter student name to search: ")

with open("students_list.json", "r") as file:
    students = json.load(file)

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("Student Found!")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student not found.")
