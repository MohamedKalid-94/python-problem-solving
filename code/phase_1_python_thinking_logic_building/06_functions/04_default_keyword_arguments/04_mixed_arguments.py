"""
Topic: Mixed Arguments

Problem:
Use positional and keyword arguments together.
"""


def student(name, age, city):
    print("Name:", name)
    print("Age :", age)
    print("City:", city)


student("Kalid", city="Chennai", age=25)
