rows = 5

for i in range(1, rows + 1):
  print(" " * (rows - i), end= " ")
  print(str(i) + " " * 1, end= " ")

for j in range(i - 1):
  print(i, end= " " )

print()
