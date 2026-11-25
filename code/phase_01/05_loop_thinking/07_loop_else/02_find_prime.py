"""
Topic: Loop else

Problem:
Check whether a number is prime.
"""

number = 13

for value in range(2, number):

    if number % value == 0:
        print("Not a Prime Number")
        break

else:
    print("Prime Number")