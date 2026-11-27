"""
=========================================================
Topic : Multiple Exceptions Handling in Python

Covered:

1. Handling multiple exceptions
2. Multiple except blocks
3. Single except with multiple errors
4. Exception hierarchy
5. Data processing error handling
6. API response error handling
7. Real-world examples

=========================================================
"""

import json
from pathlib import Path


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def multiple_except_blocks():

    separator("1. Multiple Except Blocks")

    try:

        number = int("Python")

        result = 100 / number

        print(result)


    except ValueError:

        print(
            "Invalid number conversion"
        )


    except ZeroDivisionError:

        print(
            "Cannot divide by zero"
        )



def single_except_multiple_errors():

    separator("2. Single Except Multiple Errors")


    try:

        value = int("AI")

        result = 100 / value

        print(result)


    except (
        ValueError,
        ZeroDivisionError
    ) as error:

        print(
            "Error:",
            error
        )



def file_and_json_processing():

    separator("3. File and JSON Exception Handling")


    try:

        with open(
            "config.json",
            "r"
        ) as file:

            data = json.load(file)

            print(data)


    except FileNotFoundError:

        print(
            "Configuration file missing"
        )


    except json.JSONDecodeError:

        print(
            "Invalid JSON format"
        )



def list_processing_errors():

    separator("4. List Processing Errors")


    numbers = [
        10,
        20,
        30
    ]


    try:

        index = 5

        print(
            numbers[index]
        )


    except IndexError:

        print(
            "Index does not exist"
        )



def dictionary_processing():

    separator("5. Dictionary Key Handling")


    user = {

        "name": "Kalid",

        "role": "AI Engineer"

    }


    try:

        print(
            user["experience"]
        )


    except KeyError:

        print(
            "Key does not exist"
        )



def type_error_handling():

    separator("6. Type Error Handling")


    try:

        result = "Python" + 10

        print(result)


    except TypeError:

        print(
            "Invalid data type operation"
        )



def api_response_simulation():

    separator("7. API Response Error Handling")


    response = {

        "status": "success",

        "data": None

    }


    try:

        if response["data"] is None:

            raise ValueError(
                "Empty API response"
            )


        print(
            response["data"]
        )


    except KeyError:

        print(
            "Missing API field"
        )


    except ValueError as error:

        print(
            error
        )



def batch_file_processing():

    separator("8. Batch File Processing")


    files = [

        "data1.txt",

        "missing.txt",

        "data2.txt"

    ]


    for file_name in files:

        try:

            with open(
                file_name,
                "r"
            ) as file:

                print(
                    file.read()
                )


        except FileNotFoundError:

            print(
                file_name,
                "not found"
            )


        except PermissionError:

            print(
                "Permission denied:",
                file_name
            )



def safe_data_conversion():

    separator("9. Data Conversion Pipeline")


    values = [

        "100",

        "Python",

        "200"

    ]


    results = []


    for value in values:

        try:

            results.append(
                int(value)
            )


        except ValueError:

            print(
                value,
                "cannot convert"
            )


    print(
        "Valid Data:",
        results
    )



def main():

    multiple_except_blocks()

    single_except_multiple_errors()

    file_and_json_processing()

    list_processing_errors()

    dictionary_processing()

    type_error_handling()

    api_response_simulation()

    batch_file_processing()

    safe_data_conversion()



if __name__ == "__main__":
    main()