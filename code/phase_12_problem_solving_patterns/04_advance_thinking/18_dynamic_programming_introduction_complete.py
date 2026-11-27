"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Dynamic Programming (Introduction)

Covered:

1. What is Dynamic Programming?
2. Overlapping Subproblems
3. Optimal Substructure
4. Memoization
5. Tabulation
6. Fibonacci DP
7. Climbing Stairs
8. Knapsack Introduction
9. Dynamic Programming vs Greedy
10. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Dynamic Programming Definition
# ---------------------------------------------------------

def dp_definition():

    separator(
        "1. Dynamic Programming Definition"
    )


    print(
        """
Dynamic Programming (DP) is a technique
for solving complex problems by breaking
them into smaller overlapping problems.

Main idea:

Solve smaller problems once

        ↓

Store results

        ↓

Reuse stored results


Two important properties:

1. Overlapping Subproblems

Same smaller problem appears multiple times.


2. Optimal Substructure

Solution can be built from
optimal smaller solutions.


Used in:

- Optimization problems
- Path finding
- Resource allocation
- Machine learning algorithms
        """
    )



# ---------------------------------------------------------
# 2. Recursive Fibonacci Problem
# ---------------------------------------------------------

def recursive_fibonacci_example():

    separator(
        "2. Fibonacci Without DP"
    )


    def fibonacci(n):

        if n <= 1:

            return n


        return (

            fibonacci(n-1)
            +
            fibonacci(n-2)

        )


    print(
        fibonacci(6)
    )


    print(
        """
Problem:

Same values are calculated repeatedly.

Example:

fib(5)

calls

fib(4)

fib(3)

and many repeated calculations.

DP solves this issue.
        """
    )



# ---------------------------------------------------------
# 3. Memoization
# ---------------------------------------------------------

def memoization_example():

    separator(
        "3. Memoization (Top Down DP)"
    )


    cache = {}


    def fibonacci(n):

        if n in cache:

            return cache[n]


        if n <= 1:

            return n


        cache[n] = (

            fibonacci(n-1)
            +
            fibonacci(n-2)

        )


        return cache[n]



    print(
        "Fibonacci:",
        fibonacci(10)
    )


    print(
        "Cache:",
        cache
    )



# ---------------------------------------------------------
# 4. Tabulation
# ---------------------------------------------------------

def tabulation_example():

    separator(
        "4. Tabulation (Bottom Up DP)"
    )


    n = 10


    dp = [

        0
        for _ in range(n+1)

    ]


    dp[0] = 0

    dp[1] = 1



    for i in range(
        2,
        n+1
    ):

        dp[i] = (

            dp[i-1]
            +
            dp[i-2]

        )


    print(
        "Fibonacci Table:"
    )


    print(
        dp
    )



# ---------------------------------------------------------
# 5. Climbing Stairs Problem
# ---------------------------------------------------------

def climbing_stairs_example():

    separator(
        "5. Climbing Stairs DP"
    )


    print(
        """
Problem:

A person can climb:

1 step

or

2 steps


How many ways to reach top?


Pattern:

ways(n)

=

ways(n-1)

+

ways(n-2)
        """
    )


    n = 5


    dp = [0]*(n+1)


    dp[0] = 1

    dp[1] = 1



    for i in range(
        2,
        n+1
    ):

        dp[i] = (

            dp[i-1]
            +
            dp[i-2]

        )


    print(
        "Ways:",
        dp[n]
    )



# ---------------------------------------------------------
# 6. Maximum Subarray Problem
# ---------------------------------------------------------

def maximum_subarray_example():

    separator(
        "6. Maximum Subarray DP"
    )


    numbers = [

        -2,
        1,
        -3,
        4,
        -1,
        2,
        1

    ]


    current = numbers[0]

    maximum = numbers[0]


    for number in numbers[1:]:


        current = max(

            number,

            current + number

        )


        maximum = max(

            maximum,

            current

        )


    print(
        "Maximum Sum:",
        maximum
    )



# ---------------------------------------------------------
# 7. Knapsack Introduction
# ---------------------------------------------------------

def knapsack_intro():

    separator(
        "7. Knapsack Problem Introduction"
    )


    print(
        """
Problem:

Choose items with maximum value
under weight limit.


Example:

Bag Capacity:

10 kg


Items:

Laptop  Value 100

Phone   Value 60

Book    Value 40


Need maximum value.


Used in:

- Resource allocation
- Budget planning
- AI optimization
        """
    )



# ---------------------------------------------------------
# 8. DP vs Greedy
# ---------------------------------------------------------

def dp_vs_greedy():

    separator(
        "8. Dynamic Programming vs Greedy"
    )


    print(
        """
Greedy:

Choose best current option.

Example:

Activity Selection.


Dynamic Programming:

Consider previous decisions.

Example:

Knapsack.


Greedy:

Faster

DP:

More accurate
        """
    )



# ---------------------------------------------------------
# 9. DP in Machine Learning
# ---------------------------------------------------------

def ml_dp_example():

    separator(
        "9. DP in Machine Learning"
    )


    print(
        """
Dynamic programming concepts appear in:


1. Reinforcement Learning

Finding optimal actions.


2. Markov Decision Process

Value calculation.


3. Sequence Optimization

Finding best paths.


4. Natural Language Processing

Sequence scoring.
        """
    )



# ---------------------------------------------------------
# 10. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "10. AI Engineering Example - Agent Planning"
    )


    print(
        """
AI Agent:

Goal:

Reach best solution.


Possible paths:

Path A

Path B

Path C


Agent stores previous results:

        ↓

Avoid repeated calculations

        ↓

Choose optimal path


Applications:

- AI planning
- Recommendation systems
- Route optimization
- Resource scheduling
- Model optimization
        """
    )



# ---------------------------------------------------------
# 11. Complexity Comparison
# ---------------------------------------------------------

def complexity_example():

    separator(
        "11. Complexity Comparison"
    )


    print(
        """
Fibonacci Example:


Normal Recursion:

Time:
O(2^n)


Dynamic Programming:

Time:
O(n)


Memory:

O(n)


DP improves performance
by storing previous answers.
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    dp_definition()

    recursive_fibonacci_example()

    memoization_example()

    tabulation_example()

    climbing_stairs_example()

    maximum_subarray_example()

    knapsack_intro()

    dp_vs_greedy()

    ml_dp_example()

    ai_real_world_example()

    complexity_example()



if __name__ == "__main__":

    main()