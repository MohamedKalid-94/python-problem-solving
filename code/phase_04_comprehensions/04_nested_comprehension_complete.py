"""
=========================================================
Topic : Nested Comprehension in Python

Author: Mohamed Kalid

Nested comprehension is used when we have:

- Loop inside another loop
- Multi-dimensional data
- Matrix operations
- Nested data processing


Syntax:

    [
        expression
        for outer_item in outer_iterable
        for inner_item in inner_iterable
    ]


Covered:

1. Nested loops conversion
2. Matrix creation
3. Matrix flattening
4. Cartesian products
5. Nested lists
6. Nested dictionaries
7. Data processing examples
8. AI/ML data examples

=========================================================
"""


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Nested Loop vs Comprehension
    # =====================================================

    separator("1. Nested Loop vs Comprehension")


    result = []


    for row in range(3):

        for col in range(3):

            result.append(
                (row, col)
            )


    print("Using Loop")

    print(result)



    result = [

        (row, col)

        for row in range(3)

        for col in range(3)

    ]


    print("\nUsing Nested Comprehension")

    print(result)



    # =====================================================
    # 2. Create Matrix
    # =====================================================

    separator("2. Matrix Creation")


    matrix = [

        [

            column

            for column in range(3)

        ]

        for row in range(3)

    ]


    print(matrix)



    # =====================================================
    # 3. Matrix with Values
    # =====================================================

    separator("3. Matrix Values")


    matrix = [

        [

            row * column

            for column in range(5)

        ]

        for row in range(5)

    ]


    for row in matrix:

        print(row)



    # =====================================================
    # 4. Flatten Matrix
    # =====================================================

    separator("4. Flatten Matrix")


    matrix = [

        [1, 2, 3],

        [4, 5, 6],

        [7, 8, 9]

    ]


    flattened = [

        value

        for row in matrix

        for value in row

    ]


    print(flattened)



    # =====================================================
    # 5. Flatten Nested List
    # =====================================================

    separator("5. Flatten Nested List")


    nested_list = [

        [

            "Python",

            "Java"

        ],

        [

            "C++",

            "Go"

        ]

    ]


    languages = [

        language

        for group in nested_list

        for language in group

    ]


    print(languages)



    # =====================================================
    # 6. Cartesian Product
    # =====================================================

    separator("6. Cartesian Product")


    colors = [

        "Red",

        "Blue"

    ]


    sizes = [

        "S",

        "M",

        "L"

    ]


    combinations = [

        (color, size)

        for color in colors

        for size in sizes

    ]


    print(combinations)



    # =====================================================
    # 7. Multiplication Table
    # =====================================================

    separator("7. Multiplication Table")


    table = [

        [

            row * column

            for column in range(1, 6)

        ]

        for row in range(1, 6)

    ]


    for row in table:

        print(row)



    # =====================================================
    # 8. Extract Values from Nested Dictionary
    # =====================================================

    separator("8. Nested Dictionary Processing")


    students = {


        "class_A": [

            {

                "name": "Alice",

                "marks": 90

            },

            {

                "name": "Bob",

                "marks": 80

            }

        ],


        "class_B": [

            {

                "name": "Chris",

                "marks": 95

            }

        ]

    }



    student_names = [

        student["name"]

        for class_students in students.values()

        for student in class_students

    ]


    print(student_names)



    # =====================================================
    # 9. Filter Nested Data
    # =====================================================

    separator("9. Filter Nested Data")


    high_scores = [

        student["name"]

        for class_students in students.values()

        for student in class_students

        if student["marks"] >= 90

    ]


    print(high_scores)



    # =====================================================
    # 10. Nested Dictionary Creation
    # =====================================================

    separator("10. Nested Dictionary")


    departments = [

        "AI",

        "Backend",

        "Frontend"

    ]


    teams = [

        "Team1",

        "Team2"

    ]


    organization = {


        department: {

            team: []

            for team in teams

        }

        for department in departments

    }


    print(organization)



    # =====================================================
    # 11. Image Pixel Processing Example
    # =====================================================

    separator("11. Image Data Example")


    image = [

        [255, 0, 100],

        [50, 200, 150]

    ]


    normalized = [

        [

            pixel / 255

            for pixel in row

        ]

        for row in image

    ]


    print(normalized)



    # =====================================================
    # 12. AI Embedding Processing Example
    # =====================================================

    separator("12. Embedding Processing")


    embeddings = [

        [0.1, 0.2, 0.3],

        [0.4, 0.5, 0.6]

    ]


    scaled_embeddings = [

        [

            value * 2

            for value in vector

        ]

        for vector in embeddings

    ]


    print(scaled_embeddings)



    # =====================================================
    # 13. Document Chunk Processing
    # =====================================================

    separator("13. RAG Document Processing")


    documents = [

        [

            "Python",

            "AI"

        ],

        [

            "RAG",

            "LLM"

        ]

    ]


    chunks = [

        chunk

        for document in documents

        for chunk in document

    ]


    print(chunks)



    # =====================================================
    # 14. Nested Conditions
    # =====================================================

    separator("14. Nested Conditions")


    numbers = [

        [1, 2, 3],

        [4, 5, 6],

        [7, 8, 9]

    ]


    result = [

        number

        for row in numbers

        for number in row

        if number % 2 == 0

    ]


    print(result)



    # =====================================================
    # 15. Complexity
    # =====================================================

    separator("15. Complexity")


    print(
        """
        Nested comprehension:

        For two loops:

            Time Complexity:
                O(n * m)


        Space Complexity:
                O(n * m)


        Be careful:
        Deep nesting reduces readability.

        """
    )



if __name__ == "__main__":

    main()