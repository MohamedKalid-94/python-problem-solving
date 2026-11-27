"""
=========================================================
Topic: Dictionary Comprehension and Hashing
=========================================================

Concepts Covered

1. Dictionary Comprehension
2. Conditional Dictionary Comprehension
3. Dictionary Transformation
4. Swapping Keys and Values
5. Hashing
6. Hash Tables
7. Hashable vs Non-Hashable Objects
8. Dictionary Internal Working
9. Time Complexity
10. Real-World Examples

"""

def main():

    # ==================================================
    # 1. Dictionary Comprehension
    # ==================================================

    print("=" * 60)
    print("1. Dictionary Comprehension")
    print("=" * 60)

    squares = {number: number ** 2 for number in range(1, 6)}

    print(squares)


    # ==================================================
    # 2. Conditional Dictionary Comprehension
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Conditional Dictionary Comprehension")
    print("=" * 60)

    even_numbers = {

        number: number ** 2

        for number in range(1, 11)

        if number % 2 == 0

    }

    print(even_numbers)


    # ==================================================
    # 3. Transforming Dictionary Values
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Transform Dictionary")
    print("=" * 60)

    marks = {

        "Alice": 85,

        "Bob": 90,

        "Chris": 75

    }

    updated_marks = {

        student: score + 5

        for student, score in marks.items()

    }

    print(updated_marks)


    # ==================================================
    # 4. Swapping Keys and Values
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Swapping Keys and Values")
    print("=" * 60)

    countries = {

        "IN": "India",

        "US": "United States",

        "JP": "Japan"

    }

    swapped = {

        value: key

        for key, value in countries.items()

    }

    print(swapped)


    # ==================================================
    # 5. Filtering Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Filtering Dictionary")
    print("=" * 60)

    employees = {

        "Alice": 80000,

        "Bob": 50000,

        "Chris": 90000,

        "David": 45000

    }

    high_salary = {

        name: salary

        for name, salary in employees.items()

        if salary >= 70000

    }

    print(high_salary)


    # ==================================================
    # 6. Hashing
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Hashing")
    print("=" * 60)

    print("Hash of String")

    print(hash("Python"))

    print()

    print("Hash of Integer")

    print(hash(100))

    print()

    print("Hash of Tuple")

    print(hash((10, 20)))


    # ==================================================
    # 7. Hashable vs Non-Hashable
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Hashable Objects")
    print("=" * 60)

    print("String:", hash("AI"))

    print("Integer:", hash(100))

    print("Tuple:", hash((1, 2)))

    print()

    print("List and Dictionary are NOT hashable.")

    # Uncomment to see error

    # hash([1,2])

    # hash({"A":1})


    # ==================================================
    # 8. Dictionary Internal Working
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Dictionary Internal Working")
    print("=" * 60)

    student = {

        "name": "Alice",

        "age": 22

    }

    print(student)

    print()

    print("Python stores keys using hash values.")

    print("Lookup is usually O(1).")


    # ==================================================
    # 9. Time Complexity
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Time Complexity")
    print("=" * 60)

    print("Lookup      : O(1) Average")

    print("Insertion   : O(1) Average")

    print("Update      : O(1) Average")

    print("Deletion    : O(1) Average")

    print("Iteration   : O(n)")


    # ==================================================
    # 10. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Currency Conversion")
    print("=" * 60)

    usd_prices = {

        "Laptop": 1000,

        "Phone": 600,

        "Tablet": 400

    }

    exchange_rate = 84

    inr_prices = {

        product: price * exchange_rate

        for product, price in usd_prices.items()

    }

    print(inr_prices)


if __name__ == "__main__":
    main()