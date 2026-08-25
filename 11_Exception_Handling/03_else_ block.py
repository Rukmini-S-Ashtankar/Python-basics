try:
  number = int(input("Enter a number: "))

except ValueError:
  print("Invalid input.")

else:
  print("You entered: ", number)
