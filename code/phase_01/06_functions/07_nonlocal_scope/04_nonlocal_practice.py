"""
Topic: nonlocal Practice

Problem:
Update an enclosing variable.
"""


def counter():

    value = 1

    def increase():

        nonlocal value

        value += 1

    increase()

    print(value)


counter()