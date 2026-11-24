"""
Problem:
Convert Celsius to Fahrenheit.

Pattern:
Transformation Pattern
"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


if __name__ == "__main__":
    print(celsius_to_fahrenheit(37))