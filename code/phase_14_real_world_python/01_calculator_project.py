"""
Phase 14 - Real World Python
Project 01 - Calculator
"""

from helpers import ask_number

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Calculator")

    while True:
        print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
        choice = input("Choose operation: ").strip()

        if choice == "5":
            print("Calculator Closed")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice")
            continue                       # ask for the menu again, not for numbers

        a = ask_number("Enter first number: ")
        b = ask_number("Enter second number: ")

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            try:
                print("Result:", divide(a, b))
            except ValueError as error:
                print("Error:", error)

if __name__ == "__main__":
    main()