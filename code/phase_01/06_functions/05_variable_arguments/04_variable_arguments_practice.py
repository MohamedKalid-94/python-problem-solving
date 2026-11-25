"""
Topic: Variable Arguments

Problem:
Display all marks.
"""


def show_marks(*marks):

    for mark in marks:
        print(mark)


show_marks(85, 90, 78, 88)