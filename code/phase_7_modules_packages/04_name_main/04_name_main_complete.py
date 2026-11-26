"""
=========================================================
Topic : __name__ and __main__ in Python

Covered:

1. Understanding __name__
2. Understanding __main__
3. Script execution flow
4. Module import behavior
5. Professional Python entry point

=========================================================
"""


import datetime



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def show_application_info():

    separator("1. Application Information")


    print(
        "Python Module Execution Example"
    )


    print(
        "Current Time:",
        datetime.datetime.now()
    )



def calculate_total():

    separator("2. Business Logic Function")


    numbers = [

        10,

        20,

        30

    ]


    total = sum(
        numbers
    )


    print(
        "Total:",
        total
    )


    return total



def module_information():

    separator("3. __name__ Information")


    print(
        "Current Module Name:",
        __name__
    )


    if __name__ == "__main__":

        print(
            "File is running directly"
        )

    else:

        print(
            "File is imported as module"
        )



def real_world_usage():

    separator("4. Real World Usage")


    examples = [

        "FastAPI application startup",

        "Machine learning training scripts",

        "Data processing pipelines",

        "CLI applications",

        "Automation scripts"

    ]


    for item in examples:

        print(
            "-",
            item
        )



def main():

    show_application_info()

    calculate_total()

    module_information()

    real_world_usage()



if __name__ == "__main__":

    main()