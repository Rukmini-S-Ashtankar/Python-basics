
import json

with open("students.json", "r") as file:
    student = json.load(file)

student["marks"] = 92

with open("students.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student marks updated successfully!")
print("Updated Marks:", student["marks"])
