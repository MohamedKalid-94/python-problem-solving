"""
=========================================================
Topic : List Comprehension in Python

Author: Mohamed Kalid

List comprehension provides a concise way to create lists.

Instead of writing:

    for loop
    append()

we can create lists in a single readable expression.

Syntax:

    [expression for item in iterable]

With condition:

    [expression for item in iterable if condition]


Covered:

1. Basic list comprehension
2. Transformation
3. Filtering
4. Conditional logic
5. Nested loops
6. String processing
7. Mathematical examples
8. Real-world examples
9. AI/Data processing examples

=========================================================
"""


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Loop vs List Comprehension
    # =====================================================

    separator("1. Normal Loop vs List Comprehension")


    numbers = []


    for i in range(1, 6):

        numbers.append(i)


    print("Using Loop:")

    print(numbers)



    numbers = [

        i

        for i in range(1, 6)

    ]


    print("Using List Comprehension:")

    print(numbers)



    # =====================================================
    # 2. Creating Squares
    # =====================================================

    separator("2. Square Numbers")


    squares = [

        x * x

        for x in range(1, 11)

    ]


    print(squares)



    # =====================================================
    # 3. Convert Values
    # =====================================================

    separator("3. Data Transformation")


    prices = [

        100,

        200,

        300,

        400

    ]


    discounted_prices = [

        price * 0.9

        for price in prices

    ]


    print(discounted_prices)



    # =====================================================
    # 4. Extract Characters
    # =====================================================

    separator("4. String Processing")


    word = "Python"


    characters = [

        char

        for char in word

    ]


    print(characters)



    # =====================================================
    # 5. Convert Uppercase
    # =====================================================

    separator("5. String Transformation")


    languages = [

        "python",

        "java",

        "go"

    ]


    uppercase = [

        language.upper()

        for language in languages

    ]


    print(uppercase)



    # =====================================================
    # 6. Filtering with Condition
    # =====================================================

    separator("6. Filtering Values")


    numbers = range(1, 21)


    even_numbers = [

        number

        for number in numbers

        if number % 2 == 0

    ]


    print(even_numbers)



    # =====================================================
    # 7. Odd Numbers
    # =====================================================

    separator("7. Odd Numbers")


    odd_numbers = [

        number

        for number in range(1, 20)

        if number % 2 != 0

    ]


    print(odd_numbers)



    # =====================================================
    # 8. Remove Empty Strings
    # =====================================================

    separator("8. Data Cleaning")


    names = [

        "Alice",

        "",

        "Bob",

        "",

        "Chris"

    ]


    cleaned_names = [

        name

        for name in names

        if name

    ]


    print(cleaned_names)



    # =====================================================
    # 9. Multiple Conditions
    # =====================================================

    separator("9. Multiple Conditions")


    numbers = range(1, 50)


    result = [

        x

        for x in numbers

        if x % 2 == 0

        if x % 5 == 0

    ]


    print(result)



    # =====================================================
    # 10. If Else Expression
    # =====================================================

    separator("10. If Else Expression")


    numbers = range(1, 10)


    result = [

        "Even" if x % 2 == 0 else "Odd"

        for x in numbers

    ]


    print(result)



    # =====================================================
    # 11. Nested List Example
    # =====================================================

    separator("11. Flatten Nested List")


    matrix = [

        [1, 2, 3],

        [4, 5, 6],

        [7, 8, 9]

    ]


    flattened = [

        item

        for row in matrix

        for item in row

    ]


    print(flattened)



    # =====================================================
    # 12. Find Common Elements
    # =====================================================

    separator("12. Common Elements")


    list1 = [

        1,

        2,

        3,

        4,

        5

    ]


    list2 = [

        3,

        4,

        5,

        6,

        7

    ]


    common = [

        x

        for x in list1

        if x in list2

    ]


    print(common)



    # =====================================================
    # 13. Extract File Names
    # =====================================================

    separator("13. File Processing")


    files = [

        "app.py",

        "data.csv",

        "model.py",

        "image.png"

    ]


    python_files = [

        file

        for file in files

        if file.endswith(".py")

    ]


    print(python_files)



    # =====================================================
    # 14. AI / RAG Example
    # =====================================================

    separator("14. AI Document Processing Example")


    documents = [

        {
            "id": 1,
            "content": "Python tutorial"
        },

        {
            "id": 2,
            "content": "AI Engineering"
        },

        {
            "id": 3,
            "content": "Short"
        }

    ]


    valid_documents = [

        doc["content"]

        for doc in documents

        if len(doc["content"]) > 10

    ]


    print(valid_documents)



    # =====================================================
    # 15. Token Processing Example
    # =====================================================

    separator("15. NLP Token Processing")


    sentence = "Python is powerful"


    tokens = [

        word.lower()

        for word in sentence.split()

    ]


    print(tokens)



    # =====================================================
    # 16. Replace Values
    # =====================================================

    separator("16. Replace Values")


    numbers = [

        1,

        2,

        3,

        4,

        5

    ]


    result = [

        x * 10 if x > 3 else x

        for x in numbers

    ]


    print(result)



    # =====================================================
    # 17. Time Complexity
    # =====================================================

    separator("17. Complexity")


    print(
        """
        List comprehension:

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)


        It creates a new list in memory.

        """
    )



if __name__ == "__main__":

    main()