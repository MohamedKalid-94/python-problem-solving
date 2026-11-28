"""
Phase 13 - Writing Clean Python
03 Docstrings
A docstring explains what a function does, its inputs, result and errors.
"""

import doctest
import inspect

from helpers import separator


# ---------- BAD ----------
def bad_discount(p, d):
    """Calculate discount."""            # repeats the name, says nothing new
    return p - p * d / 100


# ---------- CLEAN ----------
def calculate_discount(price, discount_percent):
    """Return the price after applying a percentage discount.

    Args:
        price: Original price (must be 0 or more).
        discount_percent: Discount from 0 to 100.

    Returns:
        The final price as a float.

    Raises:
        ValueError: If price is negative or the discount is not 0-100.

    Example:
        >>> calculate_discount(1000, 10)
        900.0
        >>> calculate_discount(200, 0)
        200.0
    """
    if price < 0:
        raise ValueError("price must be 0 or more")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return price - price * discount_percent / 100


class Student:
    """A student with a name and marks.

    Attributes:
        name: The student's name.
        marks: A list of marks (numbers).
    """

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        """Return the average of the marks (0.0 if there are no marks)."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)


def main():
    separator("BAD vs CLEAN docstring")
    print("BAD  :", bad_discount.__doc__)
    print("CLEAN:", calculate_discount.__doc__.splitlines()[0])

    separator("The full clean docstring")
    print(inspect.getdoc(calculate_discount))

    separator("Using the functions")
    print(calculate_discount(1000, 10))
    try:
        calculate_discount(1000, 150)
    except ValueError as error:
        print("ValueError:", error)

    student = Student("Kalid", [90, 80, 70])
    print(student.name, student.average())
    print(Student.__doc__.splitlines()[0])

    separator("The examples in a docstring are real tests")
    print(doctest.testmod())      # attempted=2, failed=0


if __name__ == "__main__":
    main()