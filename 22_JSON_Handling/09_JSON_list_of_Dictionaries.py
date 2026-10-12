
import json

students = [
    {"name": "Rukmini", "marks": 85},
    {"name": "Abhi", "marks": 92},
    {"name": "Tanu", "marks": 78}
]

# Save student records
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

# Read student records
with open("students.json", "r") as file:
    data = json.load(file)

total = 0

print("Student Records:")

for student in data:
    print(f"{student['name']}: {student['marks']} marks")
    total += student["marks"]

average = total / len(data)

print(f"\nAverage Marks: {average:.2f}")
