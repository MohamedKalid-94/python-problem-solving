"""
Topic: Sentinel Loop

Problem:
Enter student marks until -1 is entered.
"""

while True:

    marks = int(input("Enter marks (-1 to stop): "))

    if marks == -1:
        break

    print("Marks:", marks)

print("Input Completed")