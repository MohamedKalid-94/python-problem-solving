"""
Topic: Loop else

Problem:
Search for a number in a list.
"""

numbers = [10, 20, 30, 40, 50]

search = 30

for number in numbers:

    if number == search:
        print("Number Found")
        break

else:
    print("Number Not Found")