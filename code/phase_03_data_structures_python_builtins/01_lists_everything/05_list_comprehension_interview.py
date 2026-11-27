"""
Topic:
Python Lists - List Comprehension and Interview Problems

Concepts Covered:
1. Normal loop vs List comprehension
2. Basic list comprehension
3. Conditional list comprehension
4. Nested list comprehension
5. Transforming data
6. Filtering data
7. Flattening lists
8. Interview-based problems

"""

def main():

    # ==================================================
    # 1. Normal Loop vs List Comprehension
    # ==================================================

    print("1. Normal Loop vs List Comprehension")


    numbers = [1,2,3,4,5]


    # Using normal for loop

    squares = []

    for number in numbers:
        squares.append(number * number)


    print("Using loop:")
    print(squares)



    # Using list comprehension

    squares = [
        number * number
        for number in numbers
    ]


    print("Using list comprehension:")
    print(squares)



    # ==================================================
    # 2. Basic List Comprehension
    # ==================================================

    print("\n\n2. Basic List Comprehension")


    values = [10,20,30,40]


    doubled = [
        value * 2
        for value in values
    ]


    print("Doubled values:")
    print(doubled)



    # ==================================================
    # 3. Conditional List Comprehension
    # ==================================================

    print("\n\n3. Conditional List Comprehension")


    numbers = range(1,11)


    even_numbers = [
        number
        for number in numbers
        if number % 2 == 0
    ]


    print("Even numbers:")
    print(even_numbers)



    positive_numbers = [
        number
        for number in [-5,10,-2,20,0]
        if number > 0
    ]


    print("Positive numbers:")
    print(positive_numbers)



    # ==================================================
    # 4. Transforming Strings
    # ==================================================

    print("\n\n4. Transforming Data")


    names = [
        "python",
        "java",
        "ai"
    ]


    upper_names = [
        name.upper()
        for name in names
    ]


    print("Uppercase:")
    print(upper_names)



    # ==================================================
    # 5. If Else Inside List Comprehension
    # ==================================================

    print("\n\n5. If Else Condition")


    numbers = [1,2,3,4,5,6]


    result = [
        "Even" if number % 2 == 0 else "Odd"
        for number in numbers
    ]


    print(result)



    # ==================================================
    # 6. Nested List Comprehension
    # ==================================================

    print("\n\n6. Nested List Comprehension")


    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]


    flattened = [
        value
        for row in matrix
        for value in row
    ]


    print("Flattened Matrix:")
    print(flattened)



    # ==================================================
    # 7. Creating Matrix
    # ==================================================

    print("\n\n7. Creating Matrix")


    matrix = [
        [
            column
            for column in range(1,4)
        ]
        for row in range(3)
    ]


    print(matrix)



    # ==================================================
    # 8. Removing Duplicates
    # ==================================================

    print("\n\n8. Remove Duplicates")


    numbers = [
        1,2,2,3,4,4,5
    ]


    unique_numbers = list(
        set(numbers)
    )


    print(unique_numbers)



    # ==================================================
    # 9. Extract Values from List of Dictionaries
    # ==================================================

    print("\n\n9. List of Dictionary Processing")


    employees = [

        {
            "name":"John",
            "salary":50000
        },

        {
            "name":"David",
            "salary":70000
        },

        {
            "name":"Alex",
            "salary":40000
        }

    ]



    salaries = [
        employee["salary"]
        for employee in employees
    ]


    print("Salaries:")
    print(salaries)



    high_salary = [

        employee["name"]

        for employee in employees

        if employee["salary"] > 50000

    ]


    print("High salary employees:")
    print(high_salary)



    # ==================================================
    # 10. Interview Problem 1
    # Find common elements
    # ==================================================

    print("\n\nInterview Problem 1")


    list1 = [1,2,3,4,5]

    list2 = [3,4,5,6,7]


    common = [

        value

        for value in list1

        if value in list2

    ]


    print("Common values:")
    print(common)



    # ==================================================
    # 11. Interview Problem 2
    # Find words with length > 5
    # ==================================================

    print("\nInterview Problem 2")


    words = [
        "python",
        "AI",
        "machine",
        "code"
    ]


    long_words = [

        word

        for word in words

        if len(word) > 5

    ]


    print(long_words)



    # ==================================================
    # 12. Interview Problem 3
    # Convert Celsius to Fahrenheit
    # ==================================================

    print("\nInterview Problem 3")


    temperatures = [
        0,
        20,
        30
    ]


    fahrenheit = [

        (temp * 9/5) + 32

        for temp in temperatures

    ]


    print(fahrenheit)



if __name__ == "__main__":
    main()