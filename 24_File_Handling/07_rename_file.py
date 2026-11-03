import os

old_name = "sample.txt"
new_name = "new_sample.txt"

if os.path.exists(old_name):
  os.rename(old_name, new_name)
  print("File renamed successfully!")
else:
  print("File not found.")
