
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

words = content.split()

print("Total Words:", len(words))
print("Total Characters:", len(content))
