# Phase 14 - Real World Python
# Project 01 - Calculator

def add(a,b): return a+b

def subtract(a,b): return a-b

def multiply(a,b): return a*b

def divide(a,b):
    if b==0: return "Cannot divide by zero"
    return a/b


def main():
    print("Calculator")

    while True:
        print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")

        choice=input("Choose operation: ")

        if choice=="5":
            print("Calculator Closed")
            break

        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))

        if choice=="1":
            print("Result:",add(a,b))

        elif choice=="2":
            print("Result:",subtract(a,b))

        elif choice=="3":
            print("Result:",multiply(a,b))

        elif choice=="4":
            print("Result:",divide(a,b))

        else:
            print("Invalid choice")


if __name__=="__main__":
    main()