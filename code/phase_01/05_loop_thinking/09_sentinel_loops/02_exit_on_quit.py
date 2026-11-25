"""
Topic: Sentinel Loop

Problem:
Stop when user enters 'quit'.
"""

while True:

    text = input("Enter text (quit to stop): ")

    if text == "quit":
        break

    print("You entered:", text)

print("Program Ended")