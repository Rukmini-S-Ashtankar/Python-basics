modes = {
  "r": "Read",
  "w": "Write",
  "a": "Append",
  "x": "Create"
}

for mode, meaning in modes.items():
  print(f"{mode} -> {meaning}")
