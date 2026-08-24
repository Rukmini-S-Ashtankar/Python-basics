def reverse_string(text):
  if len(text) == 0:
    return ""
    
  return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed:", reverse_string(text))
  
