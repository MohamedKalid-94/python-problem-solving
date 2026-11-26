"""
=========================================================
Topic : Try Except Basics in Python

Covered:

1. Basic exception handling
2. ValueError handling
3. ZeroDivisionError handling
4. FileNotFoundError handling
5. User input validation
6. Safe calculation
7. Real-world examples

=========================================================
"""

from pathlib import Path


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def basic_try_except():

    separator("1. Basic Try Except")

    try:

        number = 10 / 2

        print(number)

    except Exception as error:

        print("Error:", error)



def division_by_zero():

    separator("2. Division By Zero Handling")

    try:

        number = 10 / 0

        print(number)

    except ZeroDivisionError:

        print("Cannot divide by zero")



def invalid_input_handling():

    separator("3. Invalid Input Handling")

    try:

        value = int("python")

        print(value)

    except ValueError:

        print("Invalid number format")



def user_input_validation():

    separator("4. User Input Validation")


    user_input = "25"


    try:

        age = int(user_input)


        if age < 0:

            raise ValueError(
                "Age cannot be negative"
            )


        print(
            "Valid Age:",
            age
        )


    except ValueError as error:

        print(
            "Validation Error:",
            error
        )



def file_not_found_handling():

    separator("5. File Not Found Handling")


    try:

        with open(
            "missing_file.txt",
            "r"
        ) as file:

            content = file.read()

            print(content)


    except FileNotFoundError:

        print(
            "File does not exist"
        )



def safe_calculator():

    separator("6. Safe Calculator")


    numbers = [
        (10, 2),
        (20, 0),
        (30, 5)
    ]


    for first, second in numbers:

        try:

            result = first / second

            print(
                first,
                "/",
                second,
                "=",
                result
            )


        except ZeroDivisionError:

            print(
                "Cannot divide",
                first,
                "by zero"
            )



def safe_file_writer():

    separator("7. Safe File Writer")


    file_path = Path(
        "output.txt"
    )


    try:

        file_path.write_text(
            "Python Exception Handling"
        )

        print(
            "File written successfully"
        )


    except PermissionError:

        print(
            "Permission denied"
        )



def real_world_payment_example():

    separator("8. Payment Processing Example")


    balance = 5000

    withdrawal = 7000


    try:

        if withdrawal > balance:

            raise Exception(
                "Insufficient balance"
            )


        balance -= withdrawal


        print(
            "Payment Successful"
        )


    except Exception as error:

        print(
            "Payment Failed:",
            error
        )



def main():

    basic_try_except()

    division_by_zero()

    invalid_input_handling()

    user_input_validation()

    file_not_found_handling()

    safe_calculator()

    safe_file_writer()

    real_world_payment_example()



if __name__ == "__main__":
    main()
    