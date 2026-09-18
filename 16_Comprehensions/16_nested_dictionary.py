numbers = [1, 2, 3]

table = {
    number: [number * i for i in range(1, 6)]
    for number in numbers
}

print(table)
