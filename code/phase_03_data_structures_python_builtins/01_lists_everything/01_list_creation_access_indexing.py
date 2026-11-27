"""
Topic:
Python Lists - Creation, Access, Indexing

A list is:
- Ordered
- Mutable (changeable)
- Allows duplicate values
- Allows different data types

"""

def main():

    # -------------------------------
    # 1. Creating Lists
    # -------------------------------

    # Empty list
    empty_list = []

    # List with values
    numbers = [10, 20, 30, 40]

    # Different data types
    mixed_list = [
        100,
        "Python",
        True,
        3.14
    ]

    print("Empty List:", empty_list)
    print("Numbers:", numbers)
    print("Mixed List:", mixed_list)


    # -------------------------------
    # 2. Accessing Elements
    # -------------------------------

    fruits = [
        "apple",
        "banana",
        "orange",
        "mango"
    ]

    print("\nOriginal List:")
    print(fruits)


    # Access first element
    print("First element:", fruits[0])


    # Access second element
    print("Second element:", fruits[1])


    # Access last element
    print("Last element:", fruits[-1])


    # Access second last element
    print("Second last:", fruits[-2])


    # -------------------------------
    # 3. Updating List Elements
    # -------------------------------

    fruits[1] = "grapes"

    print("\nAfter Updating:")
    print(fruits)


    # -------------------------------
    # 4. Checking Length
    # -------------------------------

    print("\nList Length:")
    print(len(fruits))


if __name__ == "__main__":
    main()