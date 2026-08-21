text = input("Enter a string: ")
count = 0

for character in text.lower():
    if character in "aeiou":
        count += 1

print("Vowels:", count)
