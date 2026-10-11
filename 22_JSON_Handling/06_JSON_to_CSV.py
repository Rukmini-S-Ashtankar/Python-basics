
import json
import csv

students = [
    {"name": "Rukmini", "age": 22, "marks": 91},
    {"name": "Abhi", "age": 23, "marks": 89},
    {"name": "Tanu", "age": 23, "marks": 78}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    data = json.load(file)

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "marks"])
    writer.writeheader()
    writer.writerows(data)

print("JSON data converted to CSV successfully!")
