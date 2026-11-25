"""
Topic: Nested Functions

Problem:
Create a function inside another function.
"""


def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()


outer()