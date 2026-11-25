"""
Topic: Nested if

Problem:
Student admission system.

Conditions:

1. Check entrance exam score
2. Check minimum age
"""


exam_score = 85

age = 18


if exam_score >= 70:

    if age >= 17:
        print("Admission Approved")

    else:
        print("Age requirement not satisfied")

else:
    print("Admission Rejected")