"""
Topic: Validation Function

Problem:
Validate age.
"""


def is_valid_age(age):

    if age >= 18:
        return True

    return False


print(is_valid_age(20))
