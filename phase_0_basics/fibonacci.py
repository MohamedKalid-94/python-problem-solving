"""Return the first n Fibonacci numbers as a list."""


def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        next_number = a + b
        a = b
        b = next_number
    return result