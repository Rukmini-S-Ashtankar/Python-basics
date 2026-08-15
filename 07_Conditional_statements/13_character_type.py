character = input("Enter a character: "))

if character.isalpha():
  print("Alphabet")
elif character.isdigit():
  print("Digit")
else:
  print("Special Character")
