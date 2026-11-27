"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Greedy Thinking Pattern

Covered:

1. What is Greedy Thinking?
2. Local Optimal Choice
3. Greedy Algorithm Structure
4. Activity Selection
5. Coin Change Concept
6. Maximum Profit
7. Interval Problems
8. Greedy vs Dynamic Programming
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Greedy Definition
# ---------------------------------------------------------

def greedy_definition():

    separator(
        "1. Greedy Thinking Definition"
    )


    print(
        """
Greedy Thinking is a problem-solving
approach where we choose the best
available option at each step.

Idea:

Make the best local decision now

        ↓

Continue until solution is reached


Greedy does NOT always guarantee
the global best solution.

It works when:

- Local choice leads to optimal result
- Problem has greedy property


Used in:

- Scheduling
- Optimization
- Networking
- Resource allocation
        """
    )



# ---------------------------------------------------------
# 2. Basic Greedy Choice
# ---------------------------------------------------------

def greedy_choice_example():

    separator(
        "2. Greedy Choice Example"
    )


    numbers = [

        5,
        10,
        20,
        50

    ]


    target = 65


    selected = []


    remaining = target



    for number in reversed(numbers):


        while remaining >= number:

            selected.append(number)

            remaining -= number



    print(
        "Selected:",
        selected
    )



# ---------------------------------------------------------
# 3. Coin Change Greedy
# ---------------------------------------------------------

def coin_change_example():

    separator(
        "3. Coin Change using Greedy"
    )


    coins = [

        25,
        10,
        5,
        1

    ]


    amount = 63


    result = []


    for coin in coins:


        while amount >= coin:

            result.append(coin)

            amount -= coin



    print(
        "Coins:",
        result
    )



# ---------------------------------------------------------
# 4. Activity Selection
# ---------------------------------------------------------

def activity_selection_example():

    separator(
        "4. Activity Selection Problem"
    )


    activities = [

        {
            "name":"Meeting A",
            "end":3
        },

        {
            "name":"Meeting B",
            "end":5
        },

        {
            "name":"Meeting C",
            "end":7
        }

    ]


    activities.sort(
        key=lambda x:x["end"]
    )


    selected = []


    last_end = 0



    for activity in activities:


        if activity["end"] >= last_end:

            selected.append(activity)

            last_end = activity["end"]



    print(
        selected
    )



# ---------------------------------------------------------
# 5. Maximum Profit
# ---------------------------------------------------------

def maximum_profit_example():

    separator(
        "5. Maximum Profit Concept"
    )


    prices = [

        100,
        180,
        260,
        310,
        40,
        535

    ]


    profit = 0


    for i in range(

        1,
        len(prices)

    ):


        if prices[i] > prices[i-1]:

            profit += (

                prices[i]
                -
                prices[i-1]

            )



    print(
        "Profit:",
        profit
    )



# ---------------------------------------------------------
# 6. Interval Scheduling
# ---------------------------------------------------------

def interval_example():

    separator(
        "6. Interval Scheduling"
    )


    intervals = [

        (1,3),

        (2,5),

        (4,6),

        (7,8)

    ]


    intervals.sort(
        key=lambda x:x[1]
    )


    selected = []


    end_time = 0



    for start,end in intervals:


        if start >= end_time:

            selected.append(
                (start,end)
            )

            end_time = end



    print(
        "Selected Intervals:",
        selected
    )



# ---------------------------------------------------------
# 7. Greedy Failure Example
# ---------------------------------------------------------

def greedy_failure_example():

    separator(
        "7. Greedy Does Not Always Work"
    )


    print(
        """
Example:

Coins:

[1,3,4]


Amount:

6


Greedy:

4 + 1 + 1

Total coins = 3


Optimal:

3 + 3

Total coins = 2


Conclusion:

Some problems require:

Dynamic Programming.
        """
    )



# ---------------------------------------------------------
# 8. Greedy vs Dynamic Programming
# ---------------------------------------------------------

def greedy_vs_dp():

    separator(
        "8. Greedy vs Dynamic Programming"
    )


    print(
        """
Greedy:

- Makes immediate best choice
- Faster
- Less memory
- Not always optimal


Dynamic Programming:

- Checks previous solutions
- Guarantees optimal solution
- More computation


Example:

Greedy:

Activity Selection


DP:

Knapsack Problem
        """
    )



# ---------------------------------------------------------
# 9. Greedy in System Design
# ---------------------------------------------------------

def system_design_example():

    separator(
        "9. Greedy in Real Systems"
    )


    print(
        """
Examples:

1. CPU Scheduling

Choose shortest task first.


2. Network Routing

Choose lowest cost path.


3. Cloud Resource Allocation

Choose available resource.


4. Load Balancing

Assign least loaded server.
        """
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. AI Engineering Example - Retrieval Ranking"
    )


    documents = [

        {
            "name":"doc1",
            "score":0.95
        },

        {
            "name":"doc2",
            "score":0.80
        },

        {
            "name":"doc3",
            "score":0.70
        }

    ]


    documents.sort(

        key=lambda x:x["score"],

        reverse=True

    )


    selected = documents[:2]


    print(
        "Top Documents:"
    )


    print(
        selected
    )


    print(
        """
AI Engineering Usage:

- Top-K retrieval
- Ranking systems
- Recommendation engines
- Resource selection
- Agent planning decisions
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    greedy_definition()

    greedy_choice_example()

    coin_change_example()

    activity_selection_example()

    maximum_profit_example()

    interval_example()

    greedy_failure_example()

    greedy_vs_dp()

    system_design_example()

    ai_real_world_example()



if __name__ == "__main__":

    main()