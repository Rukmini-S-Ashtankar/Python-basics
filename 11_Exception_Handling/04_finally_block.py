try:
  number = int(input("Enter a number: "))
  print("Number:", number)

except ValueError:
  print("Invalid input.")

finally:
  print("Program finished.")
  
