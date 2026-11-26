"""
Topic: Infinite Loop

Problem:
Continuously display numbers until stopped.
"""

number = 1

while True:

    print(number)

    if number == 10:
        break

    number = number + 1