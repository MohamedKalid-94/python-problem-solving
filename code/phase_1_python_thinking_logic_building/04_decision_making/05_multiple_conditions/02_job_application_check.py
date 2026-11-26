"""
Topic: Multiple Conditions

Problem:
Check job eligibility.

Conditions:

Experience >= 2 years
AND
Required skill available
"""


experience = 3

has_python_skill = True


if experience >= 2 and has_python_skill:

    print("Eligible for interview")

else:

    print("Not eligible")