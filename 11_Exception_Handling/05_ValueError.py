try:
  age = int(input("Enter your agee: "))
  print("Age:", age)

except ValueError:
  print("Age must be a number.")
