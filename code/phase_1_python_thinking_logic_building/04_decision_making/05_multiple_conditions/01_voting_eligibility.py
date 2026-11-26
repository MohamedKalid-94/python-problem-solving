"""
Topic: Multiple Conditions

Problem:
Check voting eligibility.

Conditions:

Age >= 18
AND
Citizen == True
"""


age = 22

is_citizen = True


if age >= 18 and is_citizen:

    print("Eligible for voting")

else:

    print("Not eligible for voting")