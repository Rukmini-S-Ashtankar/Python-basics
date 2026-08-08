numbers = (10, 20, 30, 40, 50, 60)

print("Tuple:", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("First Three:", numbers[:3])

if 30 in numbers:
  print("30 is present in the tuples.")
