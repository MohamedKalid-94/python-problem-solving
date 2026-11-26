"""
Problem:
Calculate Percentage.

Pattern:
Ratio Pattern
"""


def calculate_percentage(obtained_marks, total_marks):
    percentage = (obtained_marks / total_marks) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    print(calculate_percentage(420, 500))