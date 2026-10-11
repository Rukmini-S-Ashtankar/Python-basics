
import json

students_a = [
    {"name": "Rukmini", "marks": 85},
    {"name": "Abhi", "marks": 92}
]

students_b = [
    {"name": "Tanu", "marks": 78},
    {"name": "Ansh", "marks": 88}
]

with open("students_a.json", "w") as file:
    json.dump(students_a, file, indent=4)

with open("students_b.json", "w") as file:
    json.dump(students_b, file, indent=4)

with open("students_a.json", "r") as file:
    data_a = json.load(file)

with open("students_b.json", "r") as file:
    data_b = json.load(file)

merged_data = data_a + data_b

with open("merged_students.json", "w") as file:
    json.dump(merged_data, file, indent=4)

print("JSON files merged successfully!")
print("Total students:", len(merged_data))

for student in merged_data:
    print(student["name"], "-", student["marks"])
