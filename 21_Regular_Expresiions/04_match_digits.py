import re

text = "My order number is 12345 and my bill is 750."

numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)
