"""
Topic: Sentinel Loop

Problem:
Keep adding numbers until a negative number is entered.
"""

total = 0

while True:

    number = int(input("Enter a number: "))

    if number < 0:
        break

    total = total + number

print("Total:", total)