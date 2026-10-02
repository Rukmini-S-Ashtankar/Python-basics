import re

text = "Python is easy. Python is powerful."

result = re.findall("Python", text)

print("Matches:", result)
print("Total matches:", len(result))
