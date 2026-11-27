"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Binary Search Logic

Covered:

1. What is Binary Search?
2. Searching in Sorted Data
3. Iterative Binary Search
4. Recursive Binary Search
5. Finding First Occurrence
6. Finding Last Occurrence
7. Search Space Reduction
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Binary Search Definition
# ---------------------------------------------------------

def binary_search_definition():

    separator(
        "1. Binary Search Definition"
    )


    print(
        """
Binary Search is an efficient searching
algorithm used on sorted data.

Idea:

Check middle element

        ↓

If target is smaller:

Search left half


If target is larger:

Search right half


Complexity:

Linear Search:

O(n)


Binary Search:

O(log n)


Requirement:

Data must be sorted.
        """
    )



# ---------------------------------------------------------
# 2. Iterative Binary Search
# ---------------------------------------------------------

def iterative_binary_search():

    separator(
        "2. Iterative Binary Search"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50,
        60

    ]


    target = 40


    left = 0

    right = len(numbers)-1


    result = -1


    while left <= right:


        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            result = middle

            break


        elif numbers[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "Found Index:",
        result
    )



# ---------------------------------------------------------
# 3. Recursive Binary Search
# ---------------------------------------------------------

def recursive_binary_search():

    separator(
        "3. Recursive Binary Search"
    )


    numbers = [

        5,
        10,
        15,
        20,
        25

    ]


    target = 20


    def search(left, right):

        if left > right:

            return -1



        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            return middle



        elif numbers[middle] < target:

            return search(
                middle + 1,
                right
            )


        else:

            return search(
                left,
                middle - 1
            )



    result = search(
        0,
        len(numbers)-1
    )


    print(
        "Found Index:",
        result
    )



# ---------------------------------------------------------
# 4. Find First Occurrence
# ---------------------------------------------------------

def first_occurrence_example():

    separator(
        "4. First Occurrence"
    )


    numbers = [

        1,
        2,
        2,
        2,
        3,
        4

    ]


    target = 2


    left = 0

    right = len(numbers)-1


    result = -1


    while left <= right:


        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            result = middle

            right = middle - 1


        elif numbers[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "First Position:",
        result
    )



# ---------------------------------------------------------
# 5. Find Last Occurrence
# ---------------------------------------------------------

def last_occurrence_example():

    separator(
        "5. Last Occurrence"
    )


    numbers = [

        1,
        2,
        2,
        2,
        3,
        4

    ]


    target = 2


    left = 0

    right = len(numbers)-1


    result = -1


    while left <= right:


        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            result = middle

            left = middle + 1


        elif numbers[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "Last Position:",
        result
    )



# ---------------------------------------------------------
# 6. Search Insert Position
# ---------------------------------------------------------

def search_insert_position():

    separator(
        "6. Search Insert Position"
    )


    numbers = [

        10,
        20,
        30,
        50

    ]


    target = 40


    left = 0

    right = len(numbers)-1


    while left <= right:


        middle = (

            left + right

        ) // 2



        if numbers[middle] == target:

            print(
                "Position:",
                middle
            )

            return


        elif numbers[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "Insert Position:",
        left
    )



# ---------------------------------------------------------
# 7. Binary Search on Answer
# ---------------------------------------------------------

def binary_search_answer_space():

    separator(
        "7. Binary Search on Answer"
    )


    print(
        """
Binary Search can be applied
to possible answers.

Example:

Find minimum capacity,
maximum speed,
optimal value.


Steps:

1. Define search range

2. Check middle answer

3. Reduce search space


Used in advanced problems.
        """
    )



# ---------------------------------------------------------
# 8. Complexity Analysis
# ---------------------------------------------------------

def complexity_example():

    separator(
        "8. Complexity Analysis"
    )


    print(
        """
Array Size:

1,000,000 elements


Linear Search:

May check all elements

O(n)


Binary Search:

Only divides search area

O(log n)


Much faster for large sorted data.
        """
    )



# ---------------------------------------------------------
# 9. Real-World Search Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "9. Real-World Example - Database Index"
    )


    print(
        """
Database indexes use similar ideas.

Example:

Finding user by ID.

Without Index:

Scan every row.


With Index:

Jump directly closer
to required location.


Benefits:

- Faster queries
- Less processing
- Better scalability
        """
    )



# ---------------------------------------------------------
# 10. AI Engineering Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. AI Real-World Example - Similarity Ranking"
    )


    similarity_scores = [

        0.10,
        0.30,
        0.60,
        0.85,
        0.95

    ]


    target = 0.85


    left = 0

    right = len(similarity_scores)-1


    result = -1


    while left <= right:


        middle = (

            left + right

        ) // 2



        if similarity_scores[middle] == target:

            result = middle

            break


        elif similarity_scores[middle] < target:

            left = middle + 1


        else:

            right = middle - 1



    print(
        "Similarity Index:",
        result
    )


    print(
        """
AI Engineering Usage:

- Sorted retrieval scores
- Ranking systems
- Search optimization
- Large dataset queries
- Recommendation systems
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    binary_search_definition()

    iterative_binary_search()

    recursive_binary_search()

    first_occurrence_example()

    last_occurrence_example()

    search_insert_position()

    binary_search_answer_space()

    complexity_example()

    real_world_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()