try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied.")
