"""
Phase 15 - Interview-Level Python
08 Recursion Problems
"""

from functools import lru_cache


def factorial(n):
    if n < 0:
        raise ValueError("n must be 0 or more")
    if n == 0:                 # base case: stops the recursion
        return 1
    return n * factorial(n - 1)


@lru_cache(maxsize=None)       # remembers answers, so each fibonacci(n) is calculated once
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be 0 or more")
    if n <= 1:                 # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_numbers(n):
    if n < 0:
        raise ValueError("n must be 0 or more")
    if n == 0:                 # base case
        return 0
    return n + sum_numbers(n - 1)


def main():
    print("Factorial:", factorial(5))
    print("Fibonacci:", fibonacci(6))
    print("Fibonacci(40):", fibonacci(40))
    print("Sum:", sum_numbers(5))


if __name__ == "__main__":
    main()