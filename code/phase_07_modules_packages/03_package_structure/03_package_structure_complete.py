"""
=========================================================
Topic : Package Structure in Python

Covered:

1. Create package structure
2. Import from package
3. __init__.py usage
4. Organize reusable code
5. Real-world project structure

=========================================================
"""


from utils.math_utils import add, multiply
from utils.string_utils import clean_text, word_count



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def math_package_example():

    separator("1. Import Functions From Package")


    number1 = 10

    number2 = 5


    print(
        "Addition:",
        add(
            number1,
            number2
        )
    )


    print(
        "Multiplication:",
        multiply(
            number1,
            number2
        )
    )



def string_package_example():

    separator("2. String Utility Package")


    text = "   Python is powerful for AI   "


    cleaned_text = clean_text(
        text
    )


    print(
        "Cleaned Text:",
        cleaned_text
    )


    print(
        "Word Count:",
        word_count(
            cleaned_text
        )
    )



def package_structure_example():

    separator("3. Package Structure")


    print(
        """
A Python package contains:

project/

├── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
        """
    )



def real_world_package_usage():

    separator("4. Real World Package Usage")


    examples = [

        "AI utility packages",

        "Database service packages",

        "API client packages",

        "Authentication packages",

        "Data processing packages"

    ]


    for item in examples:

        print(
            "-",
            item
        )



def main():

    math_package_example()

    string_package_example()

    package_structure_example()

    real_world_package_usage()



if __name__ == "__main__":
    main()