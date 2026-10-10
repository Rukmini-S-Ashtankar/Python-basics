
import json

json_data = '''
{
    "name": "Rukmini",
    "age": 22,
    "skills": ["Python", "Java", "SQL"]
}
'''

student = json.loads(json_data)

print("Name:", student["name"])
print("Age:", student["age"])
print("Skills:", student["skills"])

print("Data Type:", type(student))
