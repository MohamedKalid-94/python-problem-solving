"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Filter Pattern

Covered:

1. What is Filter Pattern?
2. Filtering using Conditions
3. Even/Odd Filtering
4. Positive/Negative Filtering
5. String Filtering
6. Object Filtering
7. Filter with Lambda
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Filter Pattern Definition
# ---------------------------------------------------------

def filter_definition():

    separator(
        "1. Filter Pattern Definition"
    )


    print(
        """
Filter Pattern is a problem-solving technique
used to select elements that satisfy a condition.

Input Data

      |
      ↓

Apply Condition

      |
      ↓

Keep Required Elements


Common uses:

- Data cleaning
- Searching records
- Removing unwanted values
- Validation
- Data processing


Pattern:

result = []

for item in data:

    if condition:

        result.append(item)
        """
    )



# ---------------------------------------------------------
# 2. Basic Filter Example
# ---------------------------------------------------------

def basic_filter_example():

    separator(
        "2. Basic Filter Example"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5,
        6

    ]


    even_numbers = []


    for number in numbers:

        if number % 2 == 0:

            even_numbers.append(number)



    print(
        "Even Numbers:",
        even_numbers
    )



# ---------------------------------------------------------
# 3. Filter Odd Numbers
# ---------------------------------------------------------

def odd_number_filter():

    separator(
        "3. Odd Number Filter"
    )


    numbers = [

        10,
        15,
        20,
        25,
        30

    ]


    odd_numbers = []


    for number in numbers:

        if number % 2 != 0:

            odd_numbers.append(number)



    print(
        odd_numbers
    )



# ---------------------------------------------------------
# 4. Filter Positive Numbers
# ---------------------------------------------------------

def positive_number_filter():

    separator(
        "4. Positive Number Filter"
    )


    numbers = [

        -5,
        10,
        -2,
        20,
        0,
        30

    ]


    positive = []


    for number in numbers:

        if number > 0:

            positive.append(number)



    print(
        "Positive Numbers:",
        positive
    )



# ---------------------------------------------------------
# 5. Filter Strings
# ---------------------------------------------------------

def string_filter_example():

    separator(
        "5. String Filter"
    )


    names = [

        "AI",
        "Python",
        "ML",
        "Generative AI",
        "SQL"

    ]


    long_names = []


    for name in names:

        if len(name) > 2:

            long_names.append(name)



    print(
        long_names
    )



# ---------------------------------------------------------
# 6. Filter Dictionary Objects
# ---------------------------------------------------------

def dictionary_filter_example():

    separator(
        "6. Object Filtering"
    )


    employees = [

        {
            "name":"John",
            "salary":50000
        },

        {
            "name":"Alice",
            "salary":80000
        },

        {
            "name":"Bob",
            "salary":40000
        }

    ]


    high_salary = []


    for employee in employees:

        if employee["salary"] > 50000:

            high_salary.append(employee)



    print(
        high_salary
    )



# ---------------------------------------------------------
# 7. Filter using List Comprehension
# ---------------------------------------------------------

def list_comprehension_filter():

    separator(
        "7. List Comprehension Filter"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    squares = [

        number * number

        for number in numbers

        if number % 2 == 0

    ]


    print(
        squares
    )



# ---------------------------------------------------------
# 8. Filter using filter()
# ---------------------------------------------------------

def built_in_filter_example():

    separator(
        "8. Python filter() Function"
    )


    numbers = [

        10,
        15,
        20,
        25

    ]


    result = list(

        filter(

            lambda x: x > 15,

            numbers

        )

    )


    print(
        result
    )



# ---------------------------------------------------------
# 9. Multiple Conditions
# ---------------------------------------------------------

def multiple_condition_filter():

    separator(
        "9. Multiple Condition Filter"
    )


    users = [

        {
            "name":"Kalid",
            "active":True,
            "experience":8
        },

        {
            "name":"John",
            "active":False,
            "experience":5
        },

        {
            "name":"Alice",
            "active":True,
            "experience":3
        }

    ]


    result = []


    for user in users:

        if (
            user["active"]
            and
            user["experience"] >= 5
        ):

            result.append(user)



    print(
        result
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - RAG Document Filter"
    )


    documents = [

        {
            "name":"python.pdf",
            "score":0.95
        },

        {
            "name":"java.pdf",
            "score":0.60
        },

        {
            "name":"ai.pdf",
            "score":0.90
        }

    ]


    relevant_documents = []


    for document in documents:

        if document["score"] >= 0.80:

            relevant_documents.append(
                document
            )



    print(
        "Relevant Documents:"
    )

    print(
        relevant_documents
    )


    print(
        """
AI Engineering Usage:

- RAG retrieval filtering
- Search ranking
- Data preprocessing
- Removing low quality data
- Model evaluation
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    filter_definition()

    basic_filter_example()

    odd_number_filter()

    positive_number_filter()

    string_filter_example()

    dictionary_filter_example()

    list_comprehension_filter()

    built_in_filter_example()

    multiple_condition_filter()

    ai_real_world_example()



if __name__ == "__main__":

    main()