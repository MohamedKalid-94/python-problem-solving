"""
=========================================================
Phase 12 : Problem Solving Patterns

Topic : Recursion Pattern

Covered:

1. What is Recursion?
2. Recursive Function Structure
3. Base Case and Recursive Case
4. Factorial
5. Fibonacci
6. Sum of Numbers
7. Reverse String
8. Tree Traversal Concept
9. Backtracking Introduction
10. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ---------------------------------------------------------
# 1. Recursion Definition
# ---------------------------------------------------------

def recursion_definition():

    separator(
        "1. Recursion Pattern Definition"
    )


    print(
        """
Recursion is a technique where a function
calls itself to solve a smaller version
of the same problem.


Every recursive function has:

1. Base Case

   Condition to stop recursion.


2. Recursive Case

   Function calls itself with
   smaller input.


Example:

factorial(5)

5 * factorial(4)

5 * 4 * factorial(3)

...


Used in:

- Tree traversal
- Graph algorithms
- Divide and conquer
- Backtracking
- File systems
        """
    )



# ---------------------------------------------------------
# 2. Basic Recursive Function
# ---------------------------------------------------------

def basic_recursion_example():

    separator(
        "2. Basic Recursion Example"
    )


    def count_down(number):

        if number == 0:

            print("Done")

            return


        print(number)


        count_down(
            number - 1
        )



    count_down(5)



# ---------------------------------------------------------
# 3. Factorial Recursion
# ---------------------------------------------------------

def factorial_example():

    separator(
        "3. Factorial using Recursion"
    )


    def factorial(n):

        if n == 0:

            return 1


        return (
            n *
            factorial(n-1)
        )



    result = factorial(5)


    print(
        "Factorial:",
        result
    )



# ---------------------------------------------------------
# 4. Sum of Numbers
# ---------------------------------------------------------

def recursive_sum_example():

    separator(
        "4. Sum of Numbers using Recursion"
    )


    def calculate_sum(n):

        if n == 0:

            return 0


        return (

            n
            +
            calculate_sum(n-1)

        )



    result = calculate_sum(10)


    print(
        "Sum:",
        result
    )



# ---------------------------------------------------------
# 5. Fibonacci Recursion
# ---------------------------------------------------------

def fibonacci_example():

    separator(
        "5. Fibonacci using Recursion"
    )


    def fibonacci(n):

        if n <= 1:

            return n


        return (

            fibonacci(n-1)
            +
            fibonacci(n-2)

        )



    for i in range(8):

        print(
            fibonacci(i),
            end=" "
        )



    print()



# ---------------------------------------------------------
# 6. Reverse String Recursion
# ---------------------------------------------------------

def reverse_string_example():

    separator(
        "6. Reverse String using Recursion"
    )


    def reverse(text):

        if len(text) == 0:

            return text


        return (

            reverse(text[1:])
            +
            text[0]

        )



    result = reverse(
        "Python"
    )


    print(
        "Reverse:",
        result
    )



# ---------------------------------------------------------
# 7. Count Elements Recursion
# ---------------------------------------------------------

def count_elements_example():

    separator(
        "7. Count Elements using Recursion"
    )


    numbers = [

        10,
        20,
        30,
        40

    ]


    def count(index):

        if index == len(numbers):

            return 0


        return (

            1
            +
            count(index+1)

        )



    print(
        "Count:",
        count(0)
    )



# ---------------------------------------------------------
# 8. Recursive Search
# ---------------------------------------------------------

def recursive_search_example():

    separator(
        "8. Recursive Search"
    )


    numbers = [

        10,
        20,
        30,
        40

    ]


    target = 30


    def search(index):

        if index == len(numbers):

            return False


        if numbers[index] == target:

            return True


        return search(
            index + 1
        )



    print(
        "Found:",
        search(0)
    )



# ---------------------------------------------------------
# 9. Tree Traversal Concept
# ---------------------------------------------------------

def tree_recursion_example():

    separator(
        "9. Tree Traversal Concept"
    )


    print(
        """
Trees naturally use recursion.


Example:


        A

      /   \\

     B     C


Traversal:


Visit A

Visit left subtree

Visit right subtree


Used in:

- File systems
- HTML DOM
- Binary trees
- AI decision trees
        """
    )



# ---------------------------------------------------------
# 10. Backtracking Introduction
# ---------------------------------------------------------

def backtracking_example():

    separator(
        "10. Backtracking Introduction"
    )


    print(
        """
Backtracking is recursion
with decision making.


Pattern:

1. Choose option

2. Explore solution

3. Undo choice

4. Try another option


Examples:

- Sudoku solver
- Maze solving
- N-Queens
- Permutations
        """
    )



# ---------------------------------------------------------
# 11. Recursive File Processing
# ---------------------------------------------------------

def file_system_recursion_example():

    separator(
        "11. File System Recursion"
    )


    print(
        """
Folder Structure:


Project

 ├── src

 │    ├── app.py

 │    └── utils.py

 └── README.md



To find all files:

Visit folder

    ↓

Visit subfolders recursively

    ↓

Collect files
        """
    )



# ---------------------------------------------------------
# 12. AI Real-World Example
# ---------------------------------------------------------

def ai_real_world_example():

    separator(
        "12. AI Real-World Example - Document Tree"
    )


    documents = [

        "root",

        [

            "chapter1",

            "chapter2"

        ]

    ]


    def traverse(data):

        if isinstance(data, list):

            for item in data:

                traverse(item)

        else:

            print(
                "Processing:",
                data
            )



    traverse(documents)


    print(
        """
AI Engineering Usage:

- Recursive document processing
- Knowledge graph traversal
- Tree based search
- Agent planning
- Nested JSON processing
        """
    )



# ---------------------------------------------------------
# 13. Recursion Complexity
# ---------------------------------------------------------

def complexity_example():

    separator(
        "13. Recursion Complexity"
    )


    print(
        """
Advantages:

- Cleaner solutions
- Natural for tree problems
- Easy divide-and-conquer


Disadvantages:

- Uses extra memory
- Function call overhead
- Risk of stack overflow


Important:

Always define a proper base case.
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    recursion_definition()

    basic_recursion_example()

    factorial_example()

    recursive_sum_example()

    fibonacci_example()

    reverse_string_example()

    count_elements_example()

    recursive_search_example()

    tree_recursion_example()

    backtracking_example()

    file_system_recursion_example()

    ai_real_world_example()

    complexity_example()



if __name__ == "__main__":

    main()