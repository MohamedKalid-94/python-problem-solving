"""
Problem:
Calculate Simple Interest.

Pattern:
Formula Pattern
"""


def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


if __name__ == "__main__":
    print(simple_interest(10000, 5, 2))