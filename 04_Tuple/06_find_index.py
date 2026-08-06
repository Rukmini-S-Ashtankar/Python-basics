fruits = ("Apple", "Banana", "Mango", "Orange")

fruit = input("Enter a fruit: ")

if fruit in fruits:
  print("Index: ", fruits.index(fruit))
else:
  print("Fruit not found.")
