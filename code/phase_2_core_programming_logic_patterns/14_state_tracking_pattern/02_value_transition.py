"""
Topic: Value Transition

Problem:
Track whether values increase or decrease.
"""

numbers = [10, 12, 9, 15]

previous = numbers[0]

for current in numbers[1:]:

    if current > previous:
        print("Increasing")

    elif current < previous:
        print("Decreasing")

    else:
        print("No Change")

    previous = current