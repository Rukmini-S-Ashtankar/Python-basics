import re

text = "apple,banana;orange mango"

fruits = re.split(r"[,;\s]+", text)

print("Fruits:", fruits)
