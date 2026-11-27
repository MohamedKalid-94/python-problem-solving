"""
=========================================================
Topic : map() Function in Python

Covered:

1. Basic map()
2. map() with Lambda
3. map() with Multiple Iterables
4. map() with User-Defined Function
5. Converting Data Types
6. Processing Dictionary Values
7. Real-World Example

=========================================================
"""

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Basic map()
# ---------------------------------------------------------

def square(number):
    return number * number

def basic_map_example():
    separator("1. Basic map()")
    numbers = [1, 2, 3, 4, 5]
    squares = map(square, numbers)
    print(list(squares))

# ---------------------------------------------------------
# map() with Lambda
# ---------------------------------------------------------

def lambda_map_example():
    separator("2. map() with Lambda")
    numbers = [10, 20, 30, 40]
    doubled = map(lambda number: number * 2, numbers)
    print(list(doubled))

# ---------------------------------------------------------
# map() with Multiple Iterables
# ---------------------------------------------------------

def multiple_iterables_example():
    separator("3. map() with Multiple Iterables")
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    added = map(lambda x, y: x + y, list1, list2)
    print(list(added))

# ---------------------------------------------------------
# map() with User-Defined Function
# ---------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def user_defined_function_example():
    separator("4. User-Defined Function")
    temperatures = [0, 20, 30, 40]
    fahrenheit = map(celsius_to_fahrenheit, temperatures)
    print(list(fahrenheit))

# ---------------------------------------------------------
# Converting Data Types
# ---------------------------------------------------------

def data_type_conversion_example():
    separator("5. Data Type Conversion")
    numbers = ["1", "2", "3", "4", "5"]
    integers = map(int, numbers)
    print(list(integers))

# ---------------------------------------------------------
# Processing Dictionary Values
# ---------------------------------------------------------

def dictionary_processing_example():
    separator("6. Processing Dictionary Values")
    students = {"John": 80,"Alice": 90,"David": 85}
    updated_marks = map(lambda mark: mark + 5, students.values())
    print(list(updated_marks))

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def calculate_tax(price):
    return round(price * 1.18, 2)

def real_world_example():
    separator("7. E-Commerce Price Calculation")
    prices = [100, 250, 399, 750]
    final_prices = map(calculate_tax, prices)
    print(list(final_prices))

def main():
    basic_map_example()
    lambda_map_example()
    multiple_iterables_example()
    user_defined_function_example()
    data_type_conversion_example()
    dictionary_processing_example()
    real_world_example()

if __name__ == "__main__":
    main()