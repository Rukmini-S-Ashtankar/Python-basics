def sum_numbers(number):
  if number == 0:
    return 0
    
  return number + sum_numbers(number - 1) 

result = sum_numbers(5)

print("Sum:", result)
