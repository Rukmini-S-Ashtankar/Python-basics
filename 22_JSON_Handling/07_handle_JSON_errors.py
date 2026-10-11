
import json

json_data = '{"name": "Rukmini", "age": 22,}'

try:
    student = json.loads(json_data)
    print("Name:", student["name"])
    print("Age:", student["age"])

except json.JSONDecodeError:
    print("Error: Invalid JSON format!")

except KeyError as error:
    print("Missing key:", error)
