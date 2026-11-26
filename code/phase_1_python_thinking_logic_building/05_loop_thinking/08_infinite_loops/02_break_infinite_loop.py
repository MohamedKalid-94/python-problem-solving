"""
Topic: Infinite Loop

Problem:
Stop an infinite loop using break.
"""

count = 1

while True:

    print("Count:", count)

    if count == 5:
        break

    count = count + 1

print("Loop Stopped")
