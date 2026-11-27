"""
Topic: Scope Comparison

Problem:
Compare local and global variables.
"""

name = "Global"


def display():

    name = "Local"

    print(name)


display()

print(name)