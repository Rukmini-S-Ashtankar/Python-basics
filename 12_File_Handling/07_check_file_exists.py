import os

filename = "sample.txt"

if os.path.exists(filename):
  print("File exists.")
else:
  print("File does not exist.")
