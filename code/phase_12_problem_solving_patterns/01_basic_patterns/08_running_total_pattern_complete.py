"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Running Total Pattern

Covered:

1. What is Running Total Pattern?
2. Cumulative Sum
3. Prefix Calculation
4. Running Average
5. Running Count
6. Tracking Maximum
7. Financial Examples
8. AI Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Running Total Definition
# ---------------------------------------------------------

def running_total_definition():

    separator(
        "1. Running Total Pattern Definition"
    )


    print(
        """
Running Total Pattern keeps track of
the accumulated result while moving
through a sequence.

Instead of calculating from the beginning
every time, we maintain previous results.


Pattern:

Initialize total

       ↓

Process current element

       ↓

Update total

       ↓

Store/Use result


Common uses:

- Prefix sums
- Financial calculations
- Analytics
- Time series data
- Cumulative metrics
        """
    )



# ---------------------------------------------------------
# 2. Basic Running Total
# ---------------------------------------------------------

def basic_running_total():

    separator(
        "2. Basic Running Total"
    )


    numbers = [

        10,
        20,
        30,
        40

    ]


    total = 0


    running_totals = []


    for number in numbers:

        total += number

        running_totals.append(total)



    print(
        "Running Totals:"
    )


    print(
        running_totals
    )



# ---------------------------------------------------------
# 3. Running Sum Example
# ---------------------------------------------------------

def running_sum_example():

    separator(
        "3. Running Sum Example"
    )


    sales = [

        1000,
        2000,
        1500,
        3000

    ]


    total_sales = 0


    for sale in sales:

        total_sales += sale


        print(
            "Current Sales:",
            total_sales
        )



# ---------------------------------------------------------
# 4. Prefix Sum
# ---------------------------------------------------------

def prefix_sum_example():

    separator(
        "4. Prefix Sum"
    )


    numbers = [

        5,
        10,
        15,
        20

    ]


    prefix = [0]


    total = 0


    for number in numbers:

        total += number

        prefix.append(total)



    print(
        "Prefix Sum:"
    )


    print(
        prefix
    )



# ---------------------------------------------------------
# 5. Running Average
# ---------------------------------------------------------

def running_average_example():

    separator(
        "5. Running Average"
    )


    scores = [

        80,
        90,
        70,
        100

    ]


    total = 0

    count = 0


    for score in scores:

        total += score

        count += 1


        average = total / count


        print(
            "Average:",
            average
        )



# ---------------------------------------------------------
# 6. Running Maximum
# ---------------------------------------------------------

def running_maximum_example():

    separator(
        "6. Running Maximum"
    )


    temperatures = [

        30,
        32,
        31,
        35,
        33

    ]


    maximum = temperatures[0]


    for temperature in temperatures:

        if temperature > maximum:

            maximum = temperature



        print(
            "Highest Temperature:",
            maximum
        )



# ---------------------------------------------------------
# 7. Running Count
# ---------------------------------------------------------

def running_count_example():

    separator(
        "7. Running Count"
    )


    events = [

        "login",
        "logout",
        "login",
        "login"

    ]


    login_count = 0


    for event in events:

        if event == "login":

            login_count += 1



        print(
            "Login Count:",
            login_count
        )



# ---------------------------------------------------------
# 8. Running Balance Example
# ---------------------------------------------------------

def running_balance_example():

    separator(
        "8. Financial Running Balance"
    )


    transactions = [

        5000,
        -1000,
        2000,
        -500

    ]


    balance = 0


    for transaction in transactions:

        balance += transaction


        print(
            "Current Balance:",
            balance
        )



# ---------------------------------------------------------
# 9. Multiple Running Totals
# ---------------------------------------------------------

def multiple_running_total():

    separator(
        "9. Multiple Running Totals"
    )


    orders = [

        {
            "items":3,
            "amount":500
        },

        {
            "items":2,
            "amount":300
        },

        {
            "items":5,
            "amount":700
        }

    ]


    total_items = 0

    total_amount = 0


    for order in orders:

        total_items += order["items"]

        total_amount += order["amount"]



    print(
        "Total Items:",
        total_items
    )


    print(
        "Total Amount:",
        total_amount
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. Real-World Example - Token Usage Tracking"
    )


    api_requests = [

        {
            "tokens":1000
        },

        {
            "tokens":1500
        },

        {
            "tokens":2000
        }

    ]


    total_tokens = 0


    usage_history = []


    for request in api_requests:

        total_tokens += request["tokens"]


        usage_history.append(
            total_tokens
        )



    print(
        "Token Usage History:"
    )


    print(
        usage_history
    )


    print(
        """
AI Engineering Usage:

- LLM token monitoring
- Cost tracking
- User analytics
- Model performance metrics
- Streaming data processing
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    running_total_definition()

    basic_running_total()

    running_sum_example()

    prefix_sum_example()

    running_average_example()

    running_maximum_example()

    running_count_example()

    running_balance_example()

    multiple_running_total()

    ai_real_world_example()



if __name__ == "__main__":

    main()