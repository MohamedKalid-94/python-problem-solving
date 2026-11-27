"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Maximum / Minimum Pattern

Covered:

1. What is Maximum / Minimum Pattern?
2. Finding Maximum Value
3. Finding Minimum Value
4. Tracking Index
5. Maximum in Objects
6. Multiple Conditions
7. Using Built-in Functions
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Maximum / Minimum Definition
# ---------------------------------------------------------

def max_min_definition():

    separator(
        "1. Maximum / Minimum Pattern Definition"
    )


    print(
        """
Maximum / Minimum Pattern is used to
find the highest or lowest value from data.

Basic idea:

Initialize a variable

        ↓

Compare every element

        ↓

Update maximum/minimum value


Common uses:

- Highest score
- Lowest price
- Best result
- Worst performance
- Ranking systems
        """
    )



# ---------------------------------------------------------
# 2. Find Maximum Number
# ---------------------------------------------------------

def maximum_number_example():

    separator(
        "2. Find Maximum Number"
    )


    numbers = [

        10,
        50,
        20,
        80,
        30

    ]


    maximum = numbers[0]


    for number in numbers:

        if number > maximum:

            maximum = number



    print(
        "Maximum:",
        maximum
    )



# ---------------------------------------------------------
# 3. Find Minimum Number
# ---------------------------------------------------------

def minimum_number_example():

    separator(
        "3. Find Minimum Number"
    )


    numbers = [

        45,
        12,
        78,
        5,
        30

    ]


    minimum = numbers[0]


    for number in numbers:

        if number < minimum:

            minimum = number



    print(
        "Minimum:",
        minimum
    )



# ---------------------------------------------------------
# 4. Track Maximum Index
# ---------------------------------------------------------

def maximum_index_example():

    separator(
        "4. Maximum Value Index"
    )


    scores = [

        70,
        85,
        95,
        60

    ]


    maximum = scores[0]

    index = 0


    for i in range(len(scores)):

        if scores[i] > maximum:

            maximum = scores[i]

            index = i



    print(
        "Highest Score:",
        maximum
    )


    print(
        "Index:",
        index
    )



# ---------------------------------------------------------
# 5. Find Second Maximum
# ---------------------------------------------------------

def second_maximum_example():

    separator(
        "5. Second Maximum Value"
    )


    numbers = [

        10,
        50,
        30,
        40,
        80

    ]


    first = float("-inf")

    second = float("-inf")


    for number in numbers:


        if number > first:

            second = first

            first = number


        elif number > second:

            second = number



    print(
        "First Maximum:",
        first
    )


    print(
        "Second Maximum:",
        second
    )



# ---------------------------------------------------------
# 6. Maximum Object Value
# ---------------------------------------------------------

def object_maximum_example():

    separator(
        "6. Maximum Object Value"
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
            "salary":60000
        }

    ]


    highest = employees[0]


    for employee in employees:

        if employee["salary"] > highest["salary"]:

            highest = employee



    print(
        "Highest Salary Employee:"
    )


    print(
        highest
    )



# ---------------------------------------------------------
# 7. Maximum using max()
# ---------------------------------------------------------

def built_in_max_example():

    separator(
        "7. Built-in max() and min()"
    )


    numbers = [

        20,
        10,
        90,
        40

    ]


    print(
        "Maximum:",
        max(numbers)
    )


    print(
        "Minimum:",
        min(numbers)
    )



# ---------------------------------------------------------
# 8. Conditional Maximum
# ---------------------------------------------------------

def conditional_maximum_example():

    separator(
        "8. Conditional Maximum"
    )


    numbers = [

        5,
        20,
        35,
        50,
        70

    ]


    maximum_even = None


    for number in numbers:

        if number % 2 == 0:


            if (
                maximum_even is None
                or
                number > maximum_even
            ):

                maximum_even = number



    print(
        "Maximum Even:",
        maximum_even
    )



# ---------------------------------------------------------
# 9. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "9. Real-World Example - Highest Similarity Score"
    )


    documents = [

        {
            "name":"python.pdf",
            "score":0.82
        },

        {
            "name":"ai.pdf",
            "score":0.95
        },

        {
            "name":"ml.pdf",
            "score":0.88
        }

    ]


    best_document = documents[0]


    for document in documents:

        if (
            document["score"]
            >
            best_document["score"]
        ):

            best_document = document



    print(
        "Best Matching Document:"
    )


    print(
        best_document
    )


    print(
        """
AI Engineering Usage:

- RAG ranking
- Model selection
- Best prediction selection
- Evaluation metrics
- Recommendation systems
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    max_min_definition()

    maximum_number_example()

    minimum_number_example()

    maximum_index_example()

    second_maximum_example()

    object_maximum_example()

    built_in_max_example()

    conditional_maximum_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()