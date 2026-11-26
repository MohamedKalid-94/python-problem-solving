"""
=========================================================
Topic : Conditional Comprehension in Python

Author: Mohamed Kalid

Conditional comprehension allows us to:

1. Filter data using if condition

Syntax:

    [
        expression
        for item in iterable
        if condition
    ]


2. Apply if-else transformation

Syntax:

    [
        value_if_true if condition else value_if_false
        for item in iterable
    ]


Covered:

1. Filtering using if
2. if-else expression
3. Multiple conditions
4. Data cleaning
5. Validation
6. Real-world examples
7. AI/ML preprocessing examples

=========================================================
"""


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Basic Filtering
    # =====================================================

    separator("1. Filter Even Numbers")


    numbers = range(1, 21)


    even_numbers = [

        number

        for number in numbers

        if number % 2 == 0

    ]


    print(even_numbers)



    # =====================================================
    # 2. Filter Odd Numbers
    # =====================================================

    separator("2. Filter Odd Numbers")


    odd_numbers = [

        number

        for number in range(1, 20)

        if number % 2 != 0

    ]


    print(odd_numbers)



    # =====================================================
    # 3. Numbers Greater Than Condition
    # =====================================================

    separator("3. Filter Based on Value")


    numbers = [

        5,

        10,

        15,

        20,

        25

    ]


    result = [

        number

        for number in numbers

        if number > 10

    ]


    print(result)



    # =====================================================
    # 4. If Else Expression
    # =====================================================

    separator("4. If Else Expression")


    numbers = range(1, 10)


    result = [

        "Even" if number % 2 == 0 else "Odd"

        for number in numbers

    ]


    print(result)



    # =====================================================
    # 5. Grade Classification
    # =====================================================

    separator("5. Student Grade System")


    marks = [

        95,

        80,

        60,

        40,

        20

    ]


    grades = [

        "Pass" if mark >= 50 else "Fail"

        for mark in marks

    ]


    print(grades)



    # =====================================================
    # 6. Multiple Conditions
    # =====================================================

    separator("6. Multiple Conditions")


    numbers = range(1, 50)


    result = [

        x

        for x in numbers

        if x % 2 == 0

        if x % 5 == 0

    ]


    print(result)



    # =====================================================
    # 7. Replace Invalid Values
    # =====================================================

    separator("7. Data Cleaning")


    values = [

        10,

        None,

        20,

        None,

        30

    ]


    cleaned = [

        value

        for value in values

        if value is not None

    ]


    print(cleaned)



    # =====================================================
    # 8. Replace Missing Values
    # =====================================================

    separator("8. Missing Value Replacement")


    values = [

        10,

        None,

        30,

        None

    ]


    processed = [

        value if value is not None else 0

        for value in values

    ]


    print(processed)



    # =====================================================
    # 9. String Validation
    # =====================================================

    separator("9. String Validation")


    names = [

        "Alice",

        "",

        "Bob",

        "   ",

        "Chris"

    ]


    valid_names = [

        name

        for name in names

        if name.strip()

    ]


    print(valid_names)



    # =====================================================
    # 10. Extract Specific Files
    # =====================================================

    separator("10. File Filtering")


    files = [

        "app.py",

        "data.csv",

        "model.py",

        "image.png",

        "test.py"

    ]


    python_files = [

        file

        for file in files

        if file.endswith(".py")

    ]


    print(python_files)



    # =====================================================
    # 11. User Filtering
    # =====================================================

    separator("11. User Validation")


    users = [

        {

            "name": "Alice",

            "active": True

        },

        {

            "name": "Bob",

            "active": False

        },

        {

            "name": "Chris",

            "active": True

        }

    ]


    active_users = [

        user["name"]

        for user in users

        if user["active"]

    ]


    print(active_users)



    # =====================================================
    # 12. API Response Cleaning
    # =====================================================

    separator("12. API Data Cleaning")


    responses = [

        {

            "id": 1,

            "status": "success"

        },

        {

            "id": 2,

            "status": "failed"

        },

        {

            "id": 3,

            "status": "success"

        }

    ]


    successful_ids = [

        response["id"]

        for response in responses

        if response["status"] == "success"

    ]


    print(successful_ids)



    # =====================================================
    # 13. AI Document Filtering
    # =====================================================

    separator("13. RAG Document Filtering")


    documents = [

        {

            "id": 1,

            "content": "Python tutorial for beginners"

        },

        {

            "id": 2,

            "content": "AI"

        },

        {

            "id": 3,

            "content": "Building RAG systems using LLM"

        }

    ]



    valid_documents = [

        doc["content"]

        for doc in documents

        if len(doc["content"]) > 10

    ]


    print(valid_documents)



    # =====================================================
    # 14. Token Filtering
    # =====================================================

    separator("14. NLP Token Cleaning")


    sentence = (

        "Python AI LLM RAG"

    )


    tokens = [

        token.lower()

        for token in sentence.split()

        if len(token) > 3

    ]


    print(tokens)



    # =====================================================
    # 15. Nested Conditional Logic
    # =====================================================

    separator("15. Conditional Classification")


    numbers = range(1, 11)


    categories = [

        "Large" if x > 5 else "Small"

        for x in numbers

    ]


    print(categories)



    # =====================================================
    # 16. Dictionary with Conditions
    # =====================================================

    separator("16. Conditional Dictionary")


    employees = {

        "Alice": 90000,

        "Bob": 40000,

        "Chris": 70000

    }


    result = {

        name: (

            "Senior"

            if salary >= 70000

            else "Junior"

        )

        for name, salary in employees.items()

    }


    print(result)



    # =====================================================
    # 17. Complexity
    # =====================================================

    separator("17. Complexity")


    print(
        """
        Conditional comprehension:

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)


        Filtering reduces output size,
        but input still needs to be scanned.

        """
    )



if __name__ == "__main__":

    main()