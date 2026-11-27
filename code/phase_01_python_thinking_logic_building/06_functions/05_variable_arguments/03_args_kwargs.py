"""
Topic: *args and **kwargs

Problem:
Use both variable arguments.
"""


def display(*numbers, **details):

    print("Numbers:", numbers)
    print("Details:", details)


display(10, 20, 30, name="Kalid", city="Chennai")