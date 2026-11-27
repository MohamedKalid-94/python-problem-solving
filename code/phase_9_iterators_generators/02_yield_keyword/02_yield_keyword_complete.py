"""
=========================================================
Topic : yield Keyword in Python

Covered:

1. Generator Function
2. yield vs return
3. Multiple yield Statements
4. Generator State
5. Infinite Generator
6. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Generator Function
# ---------------------------------------------------------

def simple_generator():
    yield 1
    yield 2
    yield 3


def generator_function_example():
    separator("1. Generator Function")

    numbers = simple_generator()

    print(numbers)

    print(next(numbers))
    print(next(numbers))
    print(next(numbers))


# ---------------------------------------------------------
# yield vs return
# ---------------------------------------------------------

def return_example():
    return [1, 2, 3]


def yield_example():
    yield 1
    yield 2
    yield 3


def yield_vs_return_example():
    separator("2. yield vs return")

    result = return_example()

    print("Return Output:", result)

    generator = yield_example()

    print("Yield Output:", generator)

    for value in generator:
        print(value)


# ---------------------------------------------------------
# Multiple yield Statements
# ---------------------------------------------------------

def multiple_yield_generator():
    print("First value generated")
    yield 10

    print("Second value generated")
    yield 20

    print("Third value generated")
    yield 30


def multiple_yield_example():
    separator("3. Multiple yield Statements")

    generator = multiple_yield_generator()

    print(next(generator))
    print(next(generator))
    print(next(generator))


# ---------------------------------------------------------
# Generator State
# ---------------------------------------------------------

def state_generator():
    print("Start")

    value = yield 100

    print("Received:", value)

    yield 200


def generator_state_example():
    separator("4. Generator State")

    generator = state_generator()

    print(next(generator))

    print(generator.send("Python"))

    try:
        next(generator)
    except StopIteration:
        print("Generator completed.")


# ---------------------------------------------------------
# Infinite Generator
# ---------------------------------------------------------

def infinite_counter():
    number = 1

    while True:
        yield number
        number += 1


def infinite_generator_example():
    separator("5. Infinite Generator")

    counter = infinite_counter()

    for _ in range(5):
        print(next(counter))


# ---------------------------------------------------------
# Generator with Processing Logic
# ---------------------------------------------------------

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def processing_generator_example():
    separator("6. Generator Processing")

    numbers = range(1, 11)

    for number in even_numbers(numbers):
        print(number)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def read_large_file():
    lines = [
        "Line 1: Python",
        "Line 2: Iterator",
        "Line 3: Generator",
        "Line 4: AI"
    ]

    for line in lines:
        yield line


def real_world_example():
    separator("7. Real-World File Reader")

    for line in read_large_file():
        print(line)


def main():
    generator_function_example()
    yield_vs_return_example()
    multiple_yield_example()
    generator_state_example()
    infinite_generator_example()
    processing_generator_example()
    real_world_example()


if __name__ == "__main__":
    main()