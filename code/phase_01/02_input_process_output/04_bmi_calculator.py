"""
Problem:
Calculate BMI.

Pattern:
Formula + Decision
"""


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


if __name__ == "__main__":
    print(calculate_bmi(70, 1.75))