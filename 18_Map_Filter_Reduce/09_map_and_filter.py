numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda number: number % 2 == 0, numbers)

squares = map(lambda number: number ** 2, even_numbers)

result = list(squares)

print("Squared even numbers:", result)
