"""
Topic: Search Function

Problem:
Search a number in a list.
"""


def search(numbers, target):

    for number in numbers:

        if number == target:
            return True

    return False


numbers = [10, 20, 30, 40]

print(search(numbers, 30))