"""
Topic: Previous and Current

Problem:
Compare each value with the previous value.
"""

numbers = [10, 15, 12, 18]

previous = numbers[0]

for current in numbers[1:]:

    print("Previous:", previous, "Current:", current)

    previous = current