"""
Topic: global Keyword

Problem:
Modify a global variable.
"""

count = 10


def update():

    global count

    count = count + 5


update()

print(count)