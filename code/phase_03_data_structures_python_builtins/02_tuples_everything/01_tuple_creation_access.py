"""
Topic:
Python Tuples - Creation, Access and Indexing

Concepts Covered:
1. Creating tuples
2. Empty tuple
3. Single element tuple
4. Multiple data types
5. Accessing elements
6. Positive indexing
7. Negative indexing
8. Tuple slicing
9. Tuple immutability introduction

"""

def main():

    # ==================================================
    # 1. Creating Tuples
    # ==================================================

    print("1. Tuple Creation")
    # Empty tuple
    empty_tuple = ()
    print("Empty tuple:")
    print(empty_tuple)

    # Tuple with values
    numbers = (10,20,30,40)
    print("\nNumbers tuple:")
    print(numbers)

    # Tuple with different data types
    mixed_tuple = (100,"Python",True,3.14)
    print("\nMixed tuple:")
    print(mixed_tuple)

    # ==================================================
    # 2. Single Element Tuple
    # ==================================================

    print("\n\n2. Single Element Tuple")
    # Incorrect way
    value = (10)
    print("Without comma:")
    print(value)
    print(type(value))

    # Correct way
    single_tuple = (10,)
    print("\nWith comma:")
    print(single_tuple)
    print(type(single_tuple))

    # ==================================================
    # 3. Accessing Tuple Elements
    # ==================================================

    print("\n\n3. Accessing Elements")
    fruits = ("apple","banana","orange","mango")
    print("Tuple:")
    print(fruits)

    # First element
    print("\nFirst element:")
    print(fruits[0])

    # Second element
    print("\nSecond element:")
    print(fruits[1])

    # Last element
    print("\nLast element:")
    print(fruits[-1])

    # Second last element
    print("\nSecond last element:")
    print(fruits[-2])

    # ==================================================
    # 4. Tuple Slicing
    # ==================================================
    print("\n\n4. Tuple Slicing")
    numbers = (10,20,30,40,50)

    # Start to end
    print("All elements:")
    print(numbers[:])

    # First three elements
    print("\nFirst three:")
    print(numbers[:3])

    # Middle elements
    print("\nMiddle values:")
    print(numbers[1:4])

    # Reverse tuple
    print("\nReverse tuple:")
    print(numbers[::-1])

    # ==================================================
    # 5. Tuple Iteration
    # ==================================================

    print("\n\n5. Tuple Iteration")
    for item in fruits:
        print(item)

    # ==================================================
    # 6. Tuple Length
    # ==================================================

    print("\n\n6. Tuple Length")
    print(len(fruits))

    # ==================================================
    # 7. Tuple Immutability
    # ==================================================
    print("\n\n7. Tuple Immutability")

    colors = ("red","green","blue")
    print(colors)

    # This will cause error
    # Tuple values cannot be changed
    # colors[0] = "yellow"
    print("Tuple cannot be modified after creation")

if __name__ == "__main__":
    main()