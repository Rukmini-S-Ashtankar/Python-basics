rows = 5

for i in range(rows):
    for j in range(rows):
        if j == i or j == rows - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
