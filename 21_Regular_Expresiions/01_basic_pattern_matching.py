import re

text = "Python is easy to learn."

result = re.match("Python", text)

if result:
    print("Pattern found at the beginning.")
else:
    print("Pattern not found.")
