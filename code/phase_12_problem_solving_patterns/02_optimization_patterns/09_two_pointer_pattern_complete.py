"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Two Pointer Pattern

Covered:

1. What is Two Pointer Pattern?
2. Left and Right Pointer
3. Reverse Array
4. Pair Sum Problem
5. Remove Duplicates
6. Palindrome Checking
7. Two Pointer on Sorted Data
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Two Pointer Definition
# ---------------------------------------------------------

def two_pointer_definition():

    separator(
        "1. Two Pointer Pattern Definition"
    )


    print(
        """
Two Pointer Pattern uses two variables
to track positions in a data structure.

Usually used with:

- Arrays
- Lists
- Strings
- Sorted data


Instead of using nested loops:

O(n²)

Two pointers reduce complexity:

O(n)


Common pointer styles:

1. Left and Right Pointer

2. Slow and Fast Pointer


Example:

Left  → Start

Right → End
        """
    )



# ---------------------------------------------------------
# 2. Basic Two Pointer Example
# ---------------------------------------------------------

def basic_two_pointer_example():

    separator(
        "2. Basic Two Pointer Movement"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50

    ]


    left = 0

    right = len(numbers) - 1


    while left < right:

        print(
            numbers[left],
            numbers[right]
        )


        left += 1

        right -= 1



# ---------------------------------------------------------
# 3. Reverse Array
# ---------------------------------------------------------

def reverse_array_example():

    separator(
        "3. Reverse Array using Two Pointers"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    left = 0

    right = len(numbers)-1


    while left < right:

        numbers[left], numbers[right] = (

            numbers[right],
            numbers[left]

        )


        left += 1

        right -= 1



    print(
        "Reversed:",
        numbers
    )



# ---------------------------------------------------------
# 4. Palindrome Checking
# ---------------------------------------------------------

def palindrome_example():

    separator(
        "4. Palindrome Checking"
    )


    text = "madam"


    left = 0

    right = len(text)-1


    is_palindrome = True


    while left < right:

        if text[left] != text[right]:

            is_palindrome = False

            break


        left += 1

        right -= 1



    print(
        "Palindrome:",
        is_palindrome
    )



# ---------------------------------------------------------
# 5. Pair Sum Problem
# ---------------------------------------------------------

def pair_sum_example():

    separator(
        "5. Pair Sum Problem"
    )


    numbers = [

        1,
        2,
        3,
        4,
        6

    ]


    target = 6


    left = 0

    right = len(numbers)-1


    result = None


    while left < right:

        current_sum = (

            numbers[left]
            +
            numbers[right]

        )


        if current_sum == target:

            result = (

                numbers[left],
                numbers[right]

            )

            break


        elif current_sum < target:

            left += 1


        else:

            right -= 1



    print(
        "Pair:",
        result
    )



# ---------------------------------------------------------
# 6. Remove Duplicates
# ---------------------------------------------------------

def remove_duplicates_example():

    separator(
        "6. Remove Duplicates from Sorted Array"
    )


    numbers = [

        1,
        1,
        2,
        2,
        3

    ]


    slow = 0


    for fast in range(1, len(numbers)):

        if numbers[fast] != numbers[slow]:

            slow += 1

            numbers[slow] = numbers[fast]



    result = numbers[:slow+1]


    print(
        "Unique Values:",
        result
    )



# ---------------------------------------------------------
# 7. Move Zeroes
# ---------------------------------------------------------

def move_zeroes_example():

    separator(
        "7. Move Zeroes"
    )


    numbers = [

        0,
        1,
        0,
        3,
        12

    ]


    position = 0


    for number in numbers:

        if number != 0:

            numbers[position] = number

            position += 1



    while position < len(numbers):

        numbers[position] = 0

        position += 1



    print(
        numbers
    )



# ---------------------------------------------------------
# 8. Fast and Slow Pointer
# ---------------------------------------------------------

def fast_slow_pointer_example():

    separator(
        "8. Fast and Slow Pointer"
    )


    values = [

        1,
        2,
        3,
        4,
        5

    ]


    slow = 0

    fast = 0


    while fast < len(values):

        print(
            "Slow:",
            values[slow],
            "Fast:",
            values[fast]
        )


        slow += 1

        fast += 2



# ---------------------------------------------------------
# 9. Sorted Array Intersection
# ---------------------------------------------------------

def intersection_example():

    separator(
        "9. Sorted Array Intersection"
    )


    array1 = [

        1,
        2,
        4,
        6

    ]


    array2 = [

        2,
        3,
        4,
        7

    ]


    i = 0

    j = 0


    result = []


    while (
        i < len(array1)
        and
        j < len(array2)
    ):


        if array1[i] == array2[j]:

            result.append(array1[i])

            i += 1

            j += 1


        elif array1[i] < array2[j]:

            i += 1


        else:

            j += 1



    print(
        result
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - Similarity Matching"
    )


    scores = [

        0.10,
        0.30,
        0.50,
        0.90

    ]


    threshold = 0.80


    left = 0

    right = len(scores)-1


    matched = []


    while left <= right:


        if scores[right] >= threshold:

            matched.append(
                scores[right]
            )


        right -= 1



    print(
        "Matching Scores:",
        matched
    )


    print(
        """
AI Engineering Usage:

- Vector similarity filtering
- Sorted search optimization
- Data comparison
- Duplicate removal
- Efficient array processing
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    two_pointer_definition()

    basic_two_pointer_example()

    reverse_array_example()

    palindrome_example()

    pair_sum_example()

    remove_duplicates_example()

    move_zeroes_example()

    fast_slow_pointer_example()

    intersection_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()