"""
Topic: Decision Pattern - Decision Tree

Problem:
Employee appraisal decision.

Flow:

Performance Check
        |
        ↓
Experience Check
        |
        ↓
Final Decision
"""


performance = "good"

experience = 6


if performance == "good":

    if experience >= 5:
        print("Promotion Recommended")

    else:
        print("Salary Increment Recommended")

else:

    print("Performance Improvement Required")