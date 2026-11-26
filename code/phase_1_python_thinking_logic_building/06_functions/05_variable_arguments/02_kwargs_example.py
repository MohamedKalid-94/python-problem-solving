"""
Topic: **kwargs

Problem:
Accept keyword arguments.
"""


def student(**details):

    print("Name:", details["name"])
    print("Age :", details["age"])


student(name="Kalid", age=25)