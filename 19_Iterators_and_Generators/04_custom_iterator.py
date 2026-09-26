class Count:
    def __init__(self, limit):
        self.number = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.limit:
            value = self.number
            self.number += 1
            return value

        raise StopIteration


numbers = Count(5)

for number in numbers:
    print(number)
