fruits = {"Apple", "Banana", "Mango",  "Orange"}

fruit = input("Enter fruit to remove: ")

if fruit in fruits:
  fruits.remove(fruit)
  print("Updated Set:", fruits)
else:
  print("Fruit not found.")
