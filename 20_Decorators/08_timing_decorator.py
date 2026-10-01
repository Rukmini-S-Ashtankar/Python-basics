import time


def timer(function):
    def wrapper():
        start = time.time()

        function()

        end = time.time()

        print("Execution time:", end - start, "seconds")

    return wrapper


@timer
def calculate():
    total = 0

    for number in range(1000000):
        total += number

    print("Calculation completed")


calculate()
