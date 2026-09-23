words = ["cat", "python", "dog", "computer", "AI"]

result = list(filter(lambda word: len(word) > 3, words))

print("Long words:", result)
