
import json

student = {
    "name": "Rukmini",
    "age": 22,
    "details": {
        "course": "MCA",
        "year": 2
    },
    "marks": {
        "Python": 90,
        "DBMS": 85,
        "AI": 95
    }
}

# Save nested data to a JSON file
with open("student_details.json", "w") as file:
    json.dump(student, file, indent=4)

# Read data from the JSON file
with open("student_details.json", "r") as file:
    data = json.load(file)

print("Student Name:", data["name"])
print("Course:", data["details"]["course"])

print("\nSubject-wise Marks:")
for subject, marks in data["marks"].items():
    print(f"{subject}: {marks}")

average = sum(data["marks"].values()) / len(data["marks"])

print(f"\nAverage Marks: {average:.2f}")
