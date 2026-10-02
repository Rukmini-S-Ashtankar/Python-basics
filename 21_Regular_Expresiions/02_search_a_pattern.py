import re

text = "I am learning Python programming."

result = re.search("Python", text)

if result:
    print("Pattern found:", result.group())
    print("Position:", result.start())
else:
    print("Pattern not found.")
