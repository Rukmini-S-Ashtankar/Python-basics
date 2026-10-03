import re

text = "Python is easy and Python is useful."

words = re.findall(r"\bPython\b", text)

print("Words found:", words)
