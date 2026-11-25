"""
Topic: if elif else

Problem:
Calculate employee bonus category.

Logic:

Experience >= 10 years:
High Bonus

Experience >= 5 years:
Medium Bonus

Below 5 years:
Normal Bonus
"""


experience = 7


if experience >= 10:
    print("High Bonus")

elif experience >= 5:
    print("Medium Bonus")

else:
    print("Normal Bonus")