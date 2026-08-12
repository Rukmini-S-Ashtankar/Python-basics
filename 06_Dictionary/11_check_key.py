student = {
  "name": "Rukmini",
  "age": 22,
  "course": "MCA"
}

key = input("Enter key to search: ")

if key in student:
  print("Key exists.")
else:
  print("Key does not exist.")
