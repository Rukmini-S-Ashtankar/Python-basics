def power(base, exponent):
  if exponent == 0:
    return 1
    
  return base * power(base, exponent - 1)


print("Result:", power(2, 5))
