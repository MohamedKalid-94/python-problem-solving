"""Return n! (for example 5! = 5 x 4 x 3 x 2 x 1 = 120)."""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result