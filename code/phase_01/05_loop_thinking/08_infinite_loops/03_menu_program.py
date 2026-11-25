"""
Topic: Infinite Loop

Problem:
Simple menu using an infinite loop.
"""

while True:

    print("1. Start")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "2":
        print("Exiting Program")
        break

    print("Starting...")