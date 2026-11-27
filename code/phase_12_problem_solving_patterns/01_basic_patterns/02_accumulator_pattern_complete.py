"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Accumulator Pattern

Covered:

1. What is Accumulator Pattern?
2. Running Accumulation
3. Sum Calculation
4. Product Calculation
5. String Building
6. List Accumulation
7. Conditional Accumulation
8. Real-World Examples

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Accumulator Pattern?
# ---------------------------------------------------------

def accumulator_definition():

    separator(
        "1. Accumulator Pattern Definition"
    )


    print(
        """
Accumulator Pattern is a technique where
we maintain a variable that stores the
result while processing data step-by-step.

Common operations:

- Sum values
- Build strings
- Collect results
- Calculate totals
- Aggregate data


Pattern:

Initialize accumulator

    ↓

Loop through data

    ↓

Update accumulator

    ↓

Return final result
        """
    )



# ---------------------------------------------------------
# 2. Basic Accumulator
# ---------------------------------------------------------

def basic_accumulator_example():

    separator(
        "2. Basic Accumulator"
    )


    numbers = [

        10,
        20,
        30,
        40

    ]


    total = 0


    for number in numbers:

        total = total + number



    print(
        "Total:",
        total
    )



# ---------------------------------------------------------
# 3. Sum using Accumulator
# ---------------------------------------------------------

def sum_accumulator_example():

    separator(
        "3. Sum Calculation"
    )


    prices = [

        100,
        250,
        500,
        750

    ]


    total_price = 0


    for price in prices:

        total_price += price



    print(
        "Total Price:",
        total_price
    )



# ---------------------------------------------------------
# 4. Product Accumulator
# ---------------------------------------------------------

def product_accumulator_example():

    separator(
        "4. Product Calculation"
    )


    numbers = [

        2,
        3,
        4

    ]


    product = 1


    for number in numbers:

        product *= number



    print(
        "Product:",
        product
    )



# ---------------------------------------------------------
# 5. String Accumulator
# ---------------------------------------------------------

def string_accumulator_example():

    separator(
        "5. String Building"
    )


    words = [

        "Python",
        "is",
        "powerful"

    ]


    sentence = ""


    for word in words:

        sentence += word + " "



    print(
        sentence
    )



# ---------------------------------------------------------
# 6. List Accumulator
# ---------------------------------------------------------

def list_accumulator_example():

    separator(
        "6. List Accumulator"
    )


    numbers = [

        1,
        2,
        3,
        4,
        5

    ]


    squared_numbers = []


    for number in numbers:

        squared_numbers.append(
            number * number
        )



    print(
        "Squared Values:"
    )

    print(
        squared_numbers
    )



# ---------------------------------------------------------
# 7. Conditional Accumulator
# ---------------------------------------------------------

def conditional_accumulator_example():

    separator(
        "7. Conditional Accumulator"
    )


    numbers = [

        10,
        15,
        20,
        25,
        30

    ]


    even_sum = 0


    for number in numbers:

        if number % 2 == 0:

            even_sum += number



    print(
        "Even Sum:",
        even_sum
    )



# ---------------------------------------------------------
# 8. Multiple Accumulators
# ---------------------------------------------------------

def multiple_accumulator_example():

    separator(
        "8. Multiple Accumulators"
    )


    marks = [

        80,
        90,
        70,
        85

    ]


    total = 0

    count = 0


    for mark in marks:

        total += mark

        count += 1



    average = total / count


    print(
        "Total:",
        total
    )


    print(
        "Average:",
        average
    )



# ---------------------------------------------------------
# 9. Dictionary Accumulator
# ---------------------------------------------------------

def dictionary_accumulator_example():

    separator(
        "9. Dictionary Accumulator"
    )


    employees = [

        {
            "name":"John",
            "salary":50000
        },

        {
            "name":"Alice",
            "salary":70000
        },

        {
            "name":"Bob",
            "salary":60000
        }

    ]


    total_salary = 0


    for employee in employees:

        total_salary += (
            employee["salary"]
        )



    print(
        "Total Salary:",
        total_salary
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - Token Cost Calculation"
    )


    api_calls = [

        {
            "tokens":1000,
            "cost":0.02
        },

        {
            "tokens":2000,
            "cost":0.04
        },

        {
            "tokens":1500,
            "cost":0.03
        }

    ]


    total_tokens = 0

    total_cost = 0


    for call in api_calls:

        total_tokens += (
            call["tokens"]
        )

        total_cost += (
            call["cost"]
        )


    print(
        "Total Tokens:",
        total_tokens
    )


    print(
        "Total Cost:",
        total_cost
    )


    print(
        """
AI Engineering Usage:

- LLM token tracking
- API cost calculation
- Usage analytics
- Model evaluation metrics
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    accumulator_definition()

    basic_accumulator_example()

    sum_accumulator_example()

    product_accumulator_example()

    string_accumulator_example()

    list_accumulator_example()

    conditional_accumulator_example()

    multiple_accumulator_example()

    dictionary_accumulator_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()