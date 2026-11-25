"""
Topic: Default Arguments

Problem:
Use a default value for a parameter.
"""


def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Kalid")