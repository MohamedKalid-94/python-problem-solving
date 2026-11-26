"""
Problem:
Calculate Area of Circle.

Pattern:
Formula Pattern
"""

import math


def area_circle(radius):
    area = math.pi * radius ** 2
    return round(area, 2)


if __name__ == "__main__":
    print(area_circle(10))