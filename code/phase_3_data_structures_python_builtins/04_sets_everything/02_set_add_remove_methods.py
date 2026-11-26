"""
=========================================================
Topic: Python Sets - Add, Remove and Set Methods
=========================================================

Concepts Covered

1. add()
2. update()
3. remove()
4. discard()
5. pop()
6. clear()
7. copy()
8. Difference Between remove() and discard()
9. Real-World Examples

"""

def main():

    # ==================================================
    # 1. add()
    # ==================================================

    print("=" * 60)
    print("1. add()")
    print("=" * 60)

    languages = {"Python", "Java"}

    print("Original Set")
    print(languages)

    languages.add("C++")

    print("\nAfter add()")
    print(languages)

    # Duplicate value
    languages.add("Python")

    print("\nAdding Duplicate")
    print(languages)


    # ==================================================
    # 2. update()
    # ==================================================

    print("\n" + "=" * 60)
    print("2. update()")
    print("=" * 60)

    numbers = {10, 20, 30}

    print("Original")
    print(numbers)

    numbers.update([40, 50])

    print("\nAfter List")
    print(numbers)

    numbers.update((60, 70))

    print("\nAfter Tuple")
    print(numbers)

    numbers.update({80, 90})

    print("\nAfter Set")
    print(numbers)


    # ==================================================
    # 3. remove()
    # ==================================================

    print("\n" + "=" * 60)
    print("3. remove()")
    print("=" * 60)

    fruits = {

        "Apple",

        "Banana",

        "Orange"

    }

    print(fruits)

    fruits.remove("Banana")

    print("\nAfter remove()")
    print(fruits)

    # Uncomment to see error

    # fruits.remove("Mango")


    # ==================================================
    # 4. discard()
    # ==================================================

    print("\n" + "=" * 60)
    print("4. discard()")
    print("=" * 60)

    colors = {

        "Red",

        "Green",

        "Blue"

    }

    print(colors)

    colors.discard("Green")

    print("\nAfter discard()")
    print(colors)

    # No error even if value doesn't exist

    colors.discard("Yellow")

    print("\nDiscard Missing Value")
    print(colors)


    # ==================================================
    # 5. pop()
    # ==================================================

    print("\n" + "=" * 60)
    print("5. pop()")
    print("=" * 60)

    animals = {

        "Cat",

        "Dog",

        "Lion"

    }

    print(animals)

    removed = animals.pop()

    print("\nRemoved Element")
    print(removed)

    print("\nRemaining Set")
    print(animals)

    print("\nNote:")
    print("pop() removes a random element.")


    # ==================================================
    # 6. clear()
    # ==================================================

    print("\n" + "=" * 60)
    print("6. clear()")
    print("=" * 60)

    marks = {

        80,

        90,

        95

    }

    print(marks)

    marks.clear()

    print("\nAfter clear()")
    print(marks)


    # ==================================================
    # 7. copy()
    # ==================================================

    print("\n" + "=" * 60)
    print("7. copy()")
    print("=" * 60)

    original = {

        "Python",

        "AI",

        "ML"

    }

    copied = original.copy()

    print("Original")
    print(original)

    print("\nCopied")
    print(copied)

    copied.add("Data Science")

    print("\nAfter Modification")

    print("Original")
    print(original)

    print("Copied")
    print(copied)


    # ==================================================
    # 8. remove() vs discard()
    # ==================================================

    print("\n" + "=" * 60)
    print("8. remove() vs discard()")
    print("=" * 60)

    skills = {

        "Python",

        "SQL"

    }

    print(skills)

    print("\nremove()")

    skills.remove("SQL")

    print(skills)

    skills.add("SQL")

    print("\ndiscard()")

    skills.discard("Java")

    print(skills)

    print("\nremove() raises KeyError.")
    print("discard() ignores missing values.")


    # ==================================================
    # 9. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Student Registration")
    print("=" * 60)

    registered_students = {

        "Alice",

        "Bob",

        "Chris"

    }

    print("Original")
    print(registered_students)

    registered_students.add("David")

    registered_students.discard("Bob")

    print("\nUpdated")
    print(registered_students)


if __name__ == "__main__":
    main()