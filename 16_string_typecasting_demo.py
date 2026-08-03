name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

print("\n----- User Details -----")
print("Name:", name)
print("Age:", age)

print("\n----- String Operations -----")
print("Length of Name:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Reversed Name:", name[::-1])

print("\n----- Type Casting -----")
print("Age as Integer:", age, type(age))
print("Age as Float:", float(age), type(float(age)))
print("Age as String:", str(age), type(str(age)))
print("Age as Boolean:", bool(age), type(bool(age)))