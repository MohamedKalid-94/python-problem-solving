"""
Topic: Sentinel Loop

Problem:
Stop when user enters 0.
"""

while True:

    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    print("You entered:", number)

print("Program Ended")