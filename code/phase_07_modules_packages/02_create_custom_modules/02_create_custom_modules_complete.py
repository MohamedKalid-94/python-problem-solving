"""
=========================================================
Topic : Creating Custom Modules in Python

Covered:

1. Create custom module
2. Import custom functions
3. Reuse code
4. Module organization
5. Real-world utility module example

=========================================================
"""


import calculator



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def basic_custom_module():

    separator("1. Custom Module Import")


    number1 = 20

    number2 = 10


    print(
        "Addition:",
        calculator.add(
            number1,
            number2
        )
    )


    print(
        "Subtraction:",
        calculator.subtract(
            number1,
            number2
        )
    )


    print(
        "Multiplication:",
        calculator.multiply(
            number1,
            number2
        )
    )


    print(
        "Division:",
        calculator.divide(
            number1,
            number2
        )
    )



def reusable_functions_example():

    separator("2. Code Reusability Example")


    numbers = [
        5,
        10,
        15
    ]


    total = calculator.calculate_sum(
        numbers
    )


    print(
        "Total:",
        total
    )



def real_world_module_usage():

    separator("3. Real World Module Usage")


    print(
        "Custom modules are used for:"
    )


    examples = [

        "Database connection functions",

        "API service functions",

        "File processing utilities",

        "AI model helper functions",

        "Configuration management"

    ]


    for item in examples:

        print(
            "-",
            item
        )



def main():

    basic_custom_module()

    reusable_functions_example()

    real_world_module_usage()



if __name__ == "__main__":
    main()