
import json

student = {
    "name": "Rukmini",
    "age": 22,
    "course": "MCA",
    "marks": 85
}

with open("students.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")
