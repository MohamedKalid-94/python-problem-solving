"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Prefix Sum Pattern

Covered:

1. What is Prefix Sum?
2. Building Prefix Array
3. Range Sum Query
4. Difference Between Normal Sum and Prefix Sum
5. Subarray Sum
6. Prefix Sum with Dictionary
7. Running Calculations
8. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Prefix Sum Definition
# ---------------------------------------------------------

def prefix_sum_definition():

    separator(
        "1. Prefix Sum Pattern Definition"
    )


    print(
        """
Prefix Sum is a technique where we store
the cumulative sum of elements.

Example:

Array:

[2, 4, 6, 8]


Prefix Sum:

[0, 2, 6, 12, 20]


Benefits:

Instead of calculating range sum
again and again:

Normal approach:

O(n)


Prefix Sum:

O(1) range query


Used in:

- Analytics
- Finance
- Time series
- Data processing
        """
    )



# ---------------------------------------------------------
# 2. Create Prefix Array
# ---------------------------------------------------------

def create_prefix_array():

    separator(
        "2. Create Prefix Array"
    )


    numbers = [

        10,
        20,
        30,
        40

    ]


    prefix = [0]


    total = 0


    for number in numbers:

        total += number

        prefix.append(total)



    print(
        "Original:",
        numbers
    )


    print(
        "Prefix:",
        prefix
    )



# ---------------------------------------------------------
# 3. Prefix Sum Range Query
# ---------------------------------------------------------

def range_sum_example():

    separator(
        "3. Range Sum Query"
    )


    numbers = [

        5,
        10,
        15,
        20,
        25

    ]


    prefix = [0]


    total = 0


    for number in numbers:

        total += number

        prefix.append(total)



    left = 1

    right = 3


    range_sum = (

        prefix[right + 1]
        -
        prefix[left]

    )


    print(
        "Range Sum:",
        range_sum
    )



# ---------------------------------------------------------
# 4. Multiple Range Queries
# ---------------------------------------------------------

def multiple_range_queries():

    separator(
        "4. Multiple Range Queries"
    )


    numbers = [

        10,
        20,
        30,
        40,
        50

    ]


    prefix = [0]


    total = 0


    for number in numbers:

        total += number

        prefix.append(total)



    queries = [

        (0,2),

        (1,4),

        (2,3)

    ]


    for left,right in queries:

        result = (

            prefix[right+1]
            -
            prefix[left]

        )


        print(
            left,
            right,
            result
        )



# ---------------------------------------------------------
# 5. Subarray Sum
# ---------------------------------------------------------

def subarray_sum_example():

    separator(
        "5. Subarray Sum"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    target = 9


    prefix_sum = 0


    count = 0


    prefix_map = {

        0:1

    }


    for number in numbers:


        prefix_sum += number


        required = (
            prefix_sum - target
        )


        if required in prefix_map:

            count += prefix_map[required]



        prefix_map[prefix_sum] = (

            prefix_map.get(
                prefix_sum,
                0
            )
            +
            1

        )


    print(
        "Subarrays Found:",
        count
    )



# ---------------------------------------------------------
# 6. Prefix Product Example
# ---------------------------------------------------------

def prefix_product_example():

    separator(
        "6. Prefix Product"
    )


    numbers = [

        2,
        3,
        4

    ]


    product = 1


    prefix = []


    for number in numbers:

        product *= number

        prefix.append(product)



    print(
        prefix
    )



# ---------------------------------------------------------
# 7. Prefix Sum with Strings
# ---------------------------------------------------------

def prefix_string_example():

    separator(
        "7. Prefix String Length"
    )


    words = [

        "AI",
        "Python",
        "ML"

    ]


    prefix = [0]


    total = 0


    for word in words:

        total += len(word)

        prefix.append(total)



    print(
        prefix
    )



# ---------------------------------------------------------
# 8. Difference Array Concept
# ---------------------------------------------------------

def difference_array_example():

    separator(
        "8. Difference Array Concept"
    )


    print(
        """
Difference Array is the reverse idea
of Prefix Sum.


Used for:

- Range updates
- Large data modifications
- Efficient changes


Example:

Update many elements in O(1)

Then rebuild final array using prefix sum.
        """
    )



# ---------------------------------------------------------
# 9. Prefix Sum Comparison
# ---------------------------------------------------------

def complexity_comparison():

    separator(
        "9. Complexity Comparison"
    )


    print(
        """
Problem:
Find sum between indexes.


Without Prefix Sum:

Each query:
O(n)


With Prefix Sum:

Preprocessing:
O(n)

Each query:
O(1)


For many queries:
Prefix Sum is much faster.
        """
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - Usage Analytics"
    )


    daily_tokens = [

        1000,
        2000,
        1500,
        3000,
        2500

    ]


    prefix_usage = [0]


    total = 0


    for tokens in daily_tokens:

        total += tokens

        prefix_usage.append(total)



    print(
        "Cumulative Token Usage:"
    )


    print(
        prefix_usage
    )


    print(
        """
AI Engineering Usage:

- LLM cost tracking
- Usage analytics
- Time-series analysis
- Financial reports
- Data dashboards
- Monitoring systems
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    prefix_sum_definition()

    create_prefix_array()

    range_sum_example()

    multiple_range_queries()

    subarray_sum_example()

    prefix_product_example()

    prefix_string_example()

    difference_array_example()

    complexity_comparison()

    ai_real_world_example()



if __name__ == "__main__":

    main()