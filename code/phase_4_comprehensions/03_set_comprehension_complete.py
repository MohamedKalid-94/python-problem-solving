"""
=========================================================
Topic : Set Comprehension in Python

Author: Mohamed Kalid

Set comprehension provides a concise way to create sets.

A set:
- Stores unique values
- Removes duplicates automatically
- Does not maintain insertion order
- Supports fast membership checking


Syntax:

    {
        expression
        for item in iterable
    }


With condition:

    {
        expression
        for item in iterable
        if condition
    }


Covered:

1. Creating sets
2. Removing duplicates
3. Transforming data
4. Filtering values
5. String processing
6. Mathematical examples
7. Data cleaning
8. AI/NLP examples
9. Interview patterns

=========================================================
"""


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Loop vs Set Comprehension
    # =====================================================

    separator("1. Loop vs Set Comprehension")


    numbers = []


    for number in range(1, 6):

        numbers.append(number)


    print("Using List:")

    print(numbers)



    number_set = {

        number

        for number in range(1, 6)

    }


    print("Using Set Comprehension:")

    print(number_set)



    # =====================================================
    # 2. Remove Duplicates
    # =====================================================

    separator("2. Remove Duplicates")


    values = [

        10,

        20,

        20,

        30,

        40,

        40

    ]


    unique_values = {

        value

        for value in values

    }


    print(unique_values)



    # =====================================================
    # 3. Square Values
    # =====================================================

    separator("3. Transform Values")


    squares = {

        x * x

        for x in range(1, 11)

    }


    print(squares)



    # =====================================================
    # 4. Filter Even Numbers
    # =====================================================

    separator("4. Filtering Even Numbers")


    even_numbers = {

        x

        for x in range(1, 20)

        if x % 2 == 0

    }


    print(even_numbers)



    # =====================================================
    # 5. Filter Odd Numbers
    # =====================================================

    separator("5. Filtering Odd Numbers")


    odd_numbers = {

        x

        for x in range(1, 20)

        if x % 2 != 0

    }


    print(odd_numbers)



    # =====================================================
    # 6. Convert Strings
    # =====================================================

    separator("6. String Transformation")


    languages = [

        "python",

        "java",

        "python",

        "go"

    ]


    uppercase_languages = {

        language.upper()

        for language in languages

    }


    print(uppercase_languages)



    # =====================================================
    # 7. Unique Characters
    # =====================================================

    separator("7. Unique Characters")


    text = "programming"


    characters = {

        char

        for char in text

    }


    print(characters)



    # =====================================================
    # 8. Common Characters
    # =====================================================

    separator("8. Common Characters")


    word1 = "python"

    word2 = "typhoon"


    common = {

        char

        for char in word1

        if char in word2

    }


    print(common)



    # =====================================================
    # 9. Extract File Extensions
    # =====================================================

    separator("9. File Extensions")


    files = [

        "app.py",

        "data.csv",

        "model.py",

        "image.png",

        "test.csv"

    ]


    extensions = {

        file.split(".")[-1]

        for file in files

    }


    print(extensions)



    # =====================================================
    # 10. Word Extraction
    # =====================================================

    separator("10. Unique Words")


    sentence = """

    Python is powerful.

    Python is easy.

    AI uses Python.

    """


    words = {

        word.lower().replace(".", "")

        for word in sentence.split()

    }


    print(words)



    # =====================================================
    # 11. Data Cleaning Example
    # =====================================================

    separator("11. Data Cleaning")


    emails = [

        "user@gmail.com",

        "admin@gmail.com",

        "user@gmail.com",

        "test@yahoo.com"

    ]


    unique_emails = {

        email

        for email in emails

    }


    print(unique_emails)



    # =====================================================
    # 12. User Roles Example
    # =====================================================

    separator("12. Extract User Roles")


    users = [

        {

            "name": "Alice",

            "role": "Developer"

        },

        {

            "name": "Bob",

            "role": "Tester"

        },

        {

            "name": "Chris",

            "role": "Developer"

        }

    ]


    roles = {

        user["role"]

        for user in users

    }


    print(roles)



    # =====================================================
    # 13. AI / NLP Token Example
    # =====================================================

    separator("13. NLP Unique Tokens")


    sentence = "python python ai machine learning ai"


    tokens = {

        word

        for word in sentence.split()

    }


    print(tokens)



    # =====================================================
    # 14. RAG Document Metadata Example
    # =====================================================

    separator("14. RAG Document Topics")


    documents = [

        {

            "id": 1,

            "topic": "Python"

        },

        {

            "id": 2,

            "topic": "AI"

        },

        {

            "id": 3,

            "topic": "Python"

        }

    ]


    topics = {

        doc["topic"]

        for doc in documents

    }


    print(topics)



    # =====================================================
    # 15. Compare Two Sets
    # =====================================================

    separator("15. Common Values")


    set1 = {

        1,

        2,

        3,

        4

    }


    set2 = {

        3,

        4,

        5,

        6

    }


    common_values = {

        value

        for value in set1

        if value in set2

    }


    print(common_values)



    # =====================================================
    # 16. Conditional Expression
    # =====================================================

    separator("16. Conditional Values")


    result = {

        "Even" if x % 2 == 0 else "Odd"

        for x in range(1, 6)

    }


    print(result)



    # =====================================================
    # 17. Membership Testing
    # =====================================================

    separator("17. Fast Lookup")


    numbers = {

        x

        for x in range(100)

    }


    print(
        50 in numbers
    )


    print(
        200 in numbers
    )



    # =====================================================
    # 18. Complexity
    # =====================================================

    separator("18. Complexity")


    print(
        """
        Set comprehension:

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)


        Set lookup:
            Average O(1)

        """
    )



if __name__ == "__main__":

    main()