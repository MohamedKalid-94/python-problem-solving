"""
=========================================================
Topic : collections.Counter
Author: Mohamed Kalid

Counter is a subclass of dictionary.

It is used to count the frequency of elements.

Instead of manually counting values using a dictionary,
Counter does it automatically.

Example:

List
↓
["A", "B", "A", "C", "A"]

Counter
↓
{'A':3, 'B':1, 'C':1}

=========================================================
"""

from collections import Counter


def separator(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():

    # =====================================================
    # 1. Creating Counter from List
    # =====================================================

    separator("1. Counter from List")

    fruits = [
        "Apple",
        "Banana",
        "Apple",
        "Orange",
        "Apple",
        "Banana"
    ]

    fruit_counter = Counter(fruits)

    print(fruit_counter)


    # =====================================================
    # 2. Counter from String
    # =====================================================

    separator("2. Counter from String")

    word = "MISSISSIPPI"

    counter = Counter(word)

    print(counter)


    # =====================================================
    # 3. Counter from Tuple
    # =====================================================

    separator("3. Counter from Tuple")

    numbers = (
        10,
        20,
        10,
        30,
        10,
        20
    )

    print(Counter(numbers))


    # =====================================================
    # 4. Counter from Dictionary
    # =====================================================

    separator("4. Counter from Dictionary")

    marks = {

        "Math": 90,
        "Science": 85,
        "English": 88

    }

    counter = Counter(marks)

    print(counter)


    # =====================================================
    # 5. Access Count
    # =====================================================

    separator("5. Access Frequency")

    data = Counter("banana")

    print(data)

    print("Count of a :", data["a"])

    print("Count of n :", data["n"])

    print("Count of z :", data["z"])

    # Missing values return 0


    # =====================================================
    # 6. Updating Counter
    # =====================================================

    separator("6. update()")

    counter = Counter("apple")

    print(counter)

    counter.update("apple")

    print(counter)

    counter.update(["a", "a", "b"])

    print(counter)


    # =====================================================
    # 7. subtract()
    # =====================================================

    separator("7. subtract()")

    counter = Counter("banana")

    print(counter)

    counter.subtract("ana")

    print(counter)


    # =====================================================
    # 8. elements()
    # =====================================================

    separator("8. elements()")

    counter = Counter({

        "Apple": 3,

        "Banana": 2,

        "Orange": 1

    })

    print(counter)

    print(list(counter.elements()))


    # =====================================================
    # 9. most_common()
    # =====================================================

    separator("9. most_common()")

    text = Counter("programming")

    print(text)

    print()

    print(text.most_common())

    print()

    print(text.most_common(3))


    # =====================================================
    # 10. total()
    # =====================================================

    separator("10. total()")

    counter = Counter({

        "A": 10,

        "B": 5,

        "C": 2

    })

    print(counter)

    print(counter.total())


    # =====================================================
    # 11. Arithmetic Operations
    # =====================================================

    separator("11. Arithmetic Operations")

    counter1 = Counter({

        "A": 4,

        "B": 2,

        "C": 1

    })

    counter2 = Counter({

        "A": 2,

        "B": 5,

        "D": 4

    })

    print("Counter 1")

    print(counter1)

    print()

    print("Counter 2")

    print(counter2)

    print()

    print("Addition")

    print(counter1 + counter2)

    print()

    print("Subtraction")

    print(counter1 - counter2)

    print()

    print("Intersection")

    print(counter1 & counter2)

    print()

    print("Union")

    print(counter1 | counter2)


    # =====================================================
    # 12. Iterating Counter
    # =====================================================

    separator("12. Iterating Counter")

    counter = Counter("python")

    for key, value in counter.items():

        print(key, "->", value)


    # =====================================================
    # 13. Real World Example
    # =====================================================

    separator("13. Word Frequency")

    sentence = """
    Python is easy.
    Python is powerful.
    Python is popular.
    """

    words = sentence.lower().replace(".", "").split()

    frequency = Counter(words)

    print(frequency)

    print()

    print("Most Common Word")

    print(frequency.most_common(1))


    # =====================================================
    # 14. Student Grades
    # =====================================================

    separator("14. Student Grades")

    grades = [

        "A",

        "B",

        "A",

        "C",

        "B",

        "A",

        "A",

        "B"

    ]

    grade_counter = Counter(grades)

    print(grade_counter)


    # =====================================================
    # 15. Website Visits
    # =====================================================

    separator("15. Website Visits")

    pages = [

        "/home",

        "/login",

        "/home",

        "/products",

        "/home",

        "/login",

        "/about"

    ]

    visits = Counter(pages)

    print(visits)

    print()

    print("Most Visited Page")

    print(visits.most_common(1))


if __name__ == "__main__":
    main()