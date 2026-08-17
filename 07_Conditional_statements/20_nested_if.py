age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (Yes/No): ").lower()

if age >= 18:
  if has_id == "yes":
    print("Entry allowed.")
  else:
    print("ID required.")
else:
  print("Entry not allowed.")
