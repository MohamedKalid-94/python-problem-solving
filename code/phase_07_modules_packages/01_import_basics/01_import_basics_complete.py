"""
=========================================================
Topic : Import Basics in Python

Covered:

1. Import built-in modules
2. Import specific functions
3. Module alias
4. Using standard library modules
5. Real-world examples

=========================================================
"""


import math
import datetime
import random
import os


from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def import_math_module():

    separator("1. Math Module Import")


    number = 25


    print(
        "Square Root:",
        math.sqrt(number)
    )


    print(
        "Power:",
        math.pow(2, 5)
    )



def import_specific_function():

    separator("2. Import Specific Function")


    from math import factorial


    print(
        "Factorial:",
        factorial(5)
    )



def module_alias():

    separator("3. Module Alias")


    import datetime as dt


    current_time = dt.datetime.now()


    print(
        "Current Time:",
        current_time
    )



def random_module_example():

    separator("4. Random Module")


    numbers = [
        10,
        20,
        30,
        40,
        50
    ]


    print(
        "Random Number:",
        random.choice(numbers)
    )


    random.shuffle(numbers)


    print(
        "Shuffled List:",
        numbers
    )



def datetime_module_example():

    separator("5. Date Time Module")


    today = datetime.date.today()


    print(
        "Today:",
        today
    )


    print(
        "Year:",
        today.year
    )



def os_module_example():

    separator("6. OS Module")


    current_folder = os.getcwd()


    print(
        "Current Folder:",
        current_folder
    )



def pathlib_module_example():

    separator("7. Pathlib Module")


    file_path = Path(
        "sample.txt"
    )


    print(
        "File Name:",
        file_path.name
    )


    print(
        "Extension:",
        file_path.suffix
    )



def real_world_project_imports():

    separator("8. Real World Import Example")


    print(
        "In real projects imports are used for:"
    )


    examples = [

        "Database connection modules",

        "API service modules",

        "AI model modules",

        "Utility modules",

        "Configuration modules"

    ]


    for item in examples:

        print(
            "-",
            item
        )



def main():

    import_math_module()

    import_specific_function()

    module_alias()

    random_module_example()

    datetime_module_example()

    os_module_example()

    pathlib_module_example()

    real_world_project_imports()



if __name__ == "__main__":
    main()