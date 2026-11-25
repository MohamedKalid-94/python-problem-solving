"""
Topic: Nested if

Problem:
Employee promotion system.

Conditions:

1. Experience check
2. Performance check
"""


experience = 6

performance_rating = 5


if experience >= 5:

    if performance_rating >= 4:
        print("Promotion Approved")

    else:
        print("Improve Performance")

else:
    print("Not Eligible for Promotion")