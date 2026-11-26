"""
=========================================================
Topic : Dictionary Comprehension in Python

Author: Mohamed Kalid

Dictionary comprehension provides a concise way to create
and transform dictionaries.

Syntax:

    {
        key_expression: value_expression
        for item in iterable
    }


With condition:

    {
        key: value
        for item in iterable
        if condition
    }


Covered:

1. Creating dictionaries
2. Transforming data
3. Filtering dictionaries
4. Swapping keys and values
5. Nested dictionaries
6. JSON/API processing
7. Data transformation
8. AI/GenAI examples

=========================================================
"""


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Loop vs Dictionary Comprehension
    # =====================================================

    separator("1. Loop vs Dictionary Comprehension")


    squares = {}


    for x in range(1, 6):

        squares[x] = x * x


    print("Using Loop:")

    print(squares)



    squares = {

        x: x * x

        for x in range(1, 6)

    }


    print("Using Dictionary Comprehension:")

    print(squares)



    # =====================================================
    # 2. Create Dictionary from List
    # =====================================================

    separator("2. Create Dictionary from List")


    numbers = [

        1,

        2,

        3,

        4,

        5

    ]


    number_map = {

        x: x * x

        for x in numbers

    }


    print(number_map)



    # =====================================================
    # 3. Convert List to Dictionary with Index
    # =====================================================

    separator("3. Index Mapping")


    names = [

        "Alice",

        "Bob",

        "Chris"

    ]


    indexed_names = {

        index: name

        for index, name in enumerate(names)

    }


    print(indexed_names)



    # =====================================================
    # 4. Transform Dictionary Values
    # =====================================================

    separator("4. Transform Values")


    prices = {

        "Laptop": 1000,

        "Phone": 500,

        "Tablet": 300

    }


    discounted_prices = {

        item: price * 0.9

        for item, price in prices.items()

    }


    print(discounted_prices)



    # =====================================================
    # 5. Filter Dictionary
    # =====================================================

    separator("5. Filter Dictionary")


    marks = {

        "Alice": 90,

        "Bob": 45,

        "Chris": 75,

        "David": 30

    }


    passed_students = {

        name: score

        for name, score in marks.items()

        if score >= 50

    }


    print(passed_students)



    # =====================================================
    # 6. Multiple Conditions
    # =====================================================

    separator("6. Multiple Conditions")


    employees = {

        "Alice": 90000,

        "Bob": 40000,

        "Chris": 70000,

        "David": 30000

    }


    high_salary = {

        name: salary

        for name, salary in employees.items()

        if salary >= 70000

    }


    print(high_salary)



    # =====================================================
    # 7. Swap Keys and Values
    # =====================================================

    separator("7. Swap Keys and Values")


    data = {

        "Python": 1,

        "Java": 2,

        "C++": 3

    }


    swapped = {

        value: key

        for key, value in data.items()

    }


    print(swapped)



    # =====================================================
    # 8. Convert Dictionary Values
    # =====================================================

    separator("8. Uppercase Keys")


    languages = {

        "python": "AI",

        "java": "Backend",

        "javascript": "Frontend"

    }


    result = {

        key.upper(): value

        for key, value in languages.items()

    }


    print(result)



    # =====================================================
    # 9. Count Characters
    # =====================================================

    separator("9. Character Frequency")


    text = "python"


    char_frequency = {

        char: text.count(char)

        for char in set(text)

    }


    print(char_frequency)



    # =====================================================
    # 10. Merge Two Lists into Dictionary
    # =====================================================

    separator("10. Zip with Dictionary Comprehension")


    keys = [

        "name",

        "role",

        "experience"

    ]


    values = [

        "Kalid",

        "AI Engineer",

        8

    ]


    profile = {

        key: value

        for key, value in zip(keys, values)

    }


    print(profile)



    # =====================================================
    # 11. Nested Dictionary Creation
    # =====================================================

    separator("11. Nested Dictionary")


    students = [

        ("Alice", 90),

        ("Bob", 80),

        ("Chris", 95)

    ]


    student_data = {

        name: {

            "marks": marks,

            "status": "Pass" if marks >= 50 else "Fail"

        }

        for name, marks in students

    }


    print(student_data)



    # =====================================================
    # 12. Group Data
    # =====================================================

    separator("12. Data Grouping")


    users = [

        {

            "id": 1,

            "role": "Developer"

        },

        {

            "id": 2,

            "role": "Tester"

        }

    ]


    user_roles = {

        user["id"]: user["role"]

        for user in users

    }


    print(user_roles)



    # =====================================================
    # 13. JSON/API Transformation
    # =====================================================

    separator("13. API Response Transformation")


    api_response = [

        {

            "user_id": 101,

            "name": "Alice"

        },

        {

            "user_id": 102,

            "name": "Bob"

        }

    ]


    user_map = {

        user["user_id"]: user["name"]

        for user in api_response

    }


    print(user_map)



    # =====================================================
    # 14. AI / RAG Example
    # =====================================================

    separator("14. AI Document Metadata Mapping")


    documents = [

        {

            "id": "doc1",

            "topic": "Python"

        },

        {

            "id": "doc2",

            "topic": "AI"

        }

    ]


    metadata_store = {

        doc["id"]: doc["topic"]

        for doc in documents

    }


    print(metadata_store)



    # =====================================================
    # 15. Token ID Mapping Example
    # =====================================================

    separator("15. NLP Token Mapping")


    tokens = [

        "python",

        "ai",

        "ml"

    ]


    token_ids = {

        token: index

        for index, token in enumerate(tokens)

    }


    print(token_ids)



    # =====================================================
    # 16. Conditional Value Assignment
    # =====================================================

    separator("16. Conditional Values")


    numbers = range(1, 6)


    result = {

        x: "Even" if x % 2 == 0 else "Odd"

        for x in numbers

    }


    print(result)



    # =====================================================
    # 17. Time Complexity
    # =====================================================

    separator("17. Complexity")


    print(
        """
        Dictionary comprehension:

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)


        Creates a new dictionary.

        """
    )



if __name__ == "__main__":

    main()