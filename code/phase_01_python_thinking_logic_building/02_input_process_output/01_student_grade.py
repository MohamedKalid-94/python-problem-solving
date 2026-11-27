"""
Problem:
Calculate total marks, average marks, and percentage.

Pattern:
Input → Process → Output
"""


def student_grade(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    percentage = (total / 300) * 100

    return {
        "total": total,
        "average": average,
        "percentage": percentage
    }


if __name__ == "__main__":
    result = student_grade(85, 90, 95)

    print(result)