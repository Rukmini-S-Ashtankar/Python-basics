with open("source.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("destination.txt", "w", encoding="utf-8") as destination:
    destination.write(content)

print("File copied successfully!")
