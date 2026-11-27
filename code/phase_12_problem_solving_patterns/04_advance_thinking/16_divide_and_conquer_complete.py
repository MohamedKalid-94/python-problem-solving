"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Divide and Conquer Pattern

Covered:

1. What is Divide and Conquer?
2. Divide Step
3. Conquer Step
4. Combine Step
5. Binary Search
6. Merge Sort Concept
7. Quick Sort Concept
8. Recursive Problem Solving
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Divide and Conquer Definition
# ---------------------------------------------------------

def divide_conquer_definition():

    separator(
        "1. Divide and Conquer Definition"
    )


    print(
        """
Divide and Conquer is a problem-solving
strategy that breaks a big problem into
smaller independent problems.


Three Steps:

1. Divide

Split problem into smaller parts.


2. Conquer

Solve smaller problems recursively.


3. Combine

Merge smaller solutions.


Pattern:

Problem

   |

Divide

   |

Sub Problems

   |

Solve

   |

Combine Result


Used in:

- Sorting algorithms
- Searching
- Optimization
- Mathematical algorithms
        """
    )



# ---------------------------------------------------------
# 2. Simple Divide Example
# ---------------------------------------------------------

def divide_example():

    separator(
        "2. Divide Example"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5,
        6

    ]


    middle = len(numbers)//2


    left = numbers[:middle]

    right = numbers[middle:]


    print(
        "Left:",
        left
    )


    print(
        "Right:",
        right
    )



# ---------------------------------------------------------
# 3. Binary Search
# ---------------------------------------------------------

def binary_search_example():

    separator(
        "3. Binary Search using Divide and Conquer"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50

    ]


    target = 40


    def search(left,right):


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
        "Index:",
        result
    )



# ---------------------------------------------------------
# 4. Merge Sort Concept
# ---------------------------------------------------------

def merge_sort_example():

    separator(
        "4. Merge Sort Concept"
    )


    numbers = [

        38,
        27,
        43,
        3,
        9

    ]


    def merge_sort(data):


        if len(data) <= 1:

            return data



        middle = len(data)//2



        left = merge_sort(
            data[:middle]
        )


        right = merge_sort(
            data[middle:]
        )



        return merge(
            left,
            right
        )



    def merge(left,right):

        result = []


        i = 0

        j = 0



        while (
            i < len(left)
            and
            j < len(right)
        ):


            if left[i] < right[j]:

                result.append(
                    left[i]
                )

                i += 1


            else:

                result.append(
                    right[j]
                )

                j += 1



        result.extend(
            left[i:]
        )


        result.extend(
            right[j:]
        )


        return result



    print(
        "Sorted:",
        merge_sort(numbers)
    )



# ---------------------------------------------------------
# 5. Quick Sort Concept
# ---------------------------------------------------------

def quick_sort_example():

    separator(
        "5. Quick Sort Concept"
    )


    numbers = [

        5,
        3,
        8,
        1,
        2

    ]


    def quick_sort(data):


        if len(data) <= 1:

            return data



        pivot = data[0]



        smaller = [

            x

            for x in data[1:]

            if x <= pivot

        ]



        greater = [

            x

            for x in data[1:]

            if x > pivot

        ]



        return (

            quick_sort(smaller)

            +

            [pivot]

            +

            quick_sort(greater)

        )



    print(
        "Sorted:",
        quick_sort(numbers)
    )



# ---------------------------------------------------------
# 6. Maximum Finding
# ---------------------------------------------------------

def maximum_divide_conquer():

    separator(
        "6. Maximum using Divide and Conquer"
    )


    numbers = [

        10,
        50,
        30,
        90,
        20

    ]


    def find_max(left,right):


        if left == right:

            return numbers[left]



        middle = (

            left + right

        ) // 2



        left_max = find_max(
            left,
            middle
        )


        right_max = find_max(
            middle + 1,
            right
        )


        return max(
            left_max,
            right_max
        )



    print(
        "Maximum:",
        find_max(
            0,
            len(numbers)-1
        )
    )



# ---------------------------------------------------------
# 7. Recurrence Concept
# ---------------------------------------------------------

def recurrence_example():

    separator(
        "7. Recurrence Concept"
    )


    print(
        """
Divide and Conquer algorithms
are represented using recurrence.


Example:


Merge Sort:

T(n)

=

2T(n/2)

+

O(n)


Meaning:

Solve two smaller problems

and combine results.
        """
    )



# ---------------------------------------------------------
# 8. Advantages and Limitations
# ---------------------------------------------------------

def advantages_example():

    separator(
        "8. Advantages and Limitations"
    )


    print(
        """
Advantages:

- Faster algorithms
- Better scalability
- Parallel processing possible
- Cleaner solutions


Limitations:

- Recursive overhead
- More complex implementation
- Extra memory usage
        """
    )



# ---------------------------------------------------------
# 9. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "9. AI Real-World Example - Large Data Processing"
    )


    print(
        """
Large AI systems divide work.


Example:

Large document collection

        |

Split into smaller chunks

        |

Process chunks separately

        |

Combine results


Applications:

- Distributed AI pipelines
- MapReduce
- Large dataset processing
- Parallel model evaluation
- Search optimization
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    divide_conquer_definition()

    divide_example()

    binary_search_example()

    merge_sort_example()

    quick_sort_example()

    maximum_divide_conquer()

    recurrence_example()

    advantages_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()