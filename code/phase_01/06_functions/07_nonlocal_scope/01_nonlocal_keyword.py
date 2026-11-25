"""
Topic: nonlocal Keyword

Problem:
Modify an enclosing variable.
"""


def outer():

    count = 10

    def inner():

        nonlocal count

        count = count + 5

    inner()

    print(count)


outer()