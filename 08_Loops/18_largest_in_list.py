numbers = [25, 10, 45, 30, 15]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)
