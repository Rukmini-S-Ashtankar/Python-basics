numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
  filter(lambda number: number % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)
