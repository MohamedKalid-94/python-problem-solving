"""
=========================================================
Topic: Python Sets - Interview Examples
=========================================================

Concepts Covered

1. Remove Duplicates
2. Find Common Elements
3. Find Unique Elements
4. Check Subset
5. Check Superset
6. Check Disjoint Sets
7. Find Missing Numbers
8. Duplicate Detection
9. Common Characters
10. Real-World Examples

Author : Mohamed Kalid
=========================================================
"""


def main():

    # ==================================================
    # 1. Remove Duplicates
    # ==================================================

    print("=" * 60)
    print("1. Remove Duplicates")
    print("=" * 60)

    numbers = [10, 20, 20, 30, 30, 40, 40, 50]

    print("Original List")
    print(numbers)

    unique_numbers = list(set(numbers))

    print("\nUnique Values")
    print(unique_numbers)

    print("-" * 60)

    # ==================================================
    # 2. Find Common Elements
    # ==================================================

    print("\n2. Find Common Elements")

    python_students = {

        "Alice",

        "Bob",

        "Chris",

        "David"

    }

    ai_students = {

        "Chris",

        "David",

        "Eva",

        "John"

    }

    common = python_students & ai_students

    print(common)

    print("-" * 60)

    # ==================================================
    # 3. Find Unique Elements
    # ==================================================

    print("\n3. Unique Elements")

    print(python_students ^ ai_students)

    print("-" * 60)

    # ==================================================
    # 4. Students Only in Python
    # ==================================================

    print("\n4. Students Only in Python")

    print(python_students - ai_students)

    print("-" * 60)

    # ==================================================
    # 5. Students Only in AI
    # ==================================================

    print("\n5. Students Only in AI")

    print(ai_students - python_students)

    print("-" * 60)

    # ==================================================
    # 6. Subset Example
    # ==================================================

    print("\n6. Subset Example")

    registered = {

        "Alice",

        "Bob",

        "Chris",

        "David"

    }

    attendees = {

        "Alice",

        "Bob"

    }

    print(attendees.issubset(registered))

    print("-" * 60)

    # ==================================================
    # 7. Superset Example
    # ==================================================

    print("\n7. Superset Example")

    print(registered.issuperset(attendees))

    print("-" * 60)

    # ==================================================
    # 8. Disjoint Example
    # ==================================================

    print("\n8. Disjoint Example")

    morning_batch = {

        "Alice",

        "Bob"

    }

    evening_batch = {

        "Chris",

        "David"

    }

    print(morning_batch.isdisjoint(evening_batch))

    print("-" * 60)

    # ==================================================
    # 9. Duplicate Detection
    # ==================================================

    print("\n9. Duplicate Detection")

    data = [10, 20, 30, 20, 40, 10, 50]

    seen = set()

    duplicates = set()

    for number in data:

        if number in seen:

            duplicates.add(number)

        else:

            seen.add(number)

    print("Duplicates")

    print(duplicates)

    print("-" * 60)

    # ==================================================
    # 10. Missing Numbers
    # ==================================================

    print("\n10. Missing Numbers")

    expected = set(range(1, 11))

    received = {

        1,

        2,

        3,

        5,

        7,

        9,

        10

    }

    print(expected - received)

    print("-" * 60)

    # ==================================================
    # 11. Common Characters
    # ==================================================

    print("\n11. Common Characters")

    word1 = "python"

    word2 = "typhoon"

    common_letters = set(word1) & set(word2)

    print(common_letters)

    print("-" * 60)

    # ==================================================
    # 12. Unique Words
    # ==================================================

    print("\n12. Unique Words")

    sentence = "python is easy python is powerful"

    words = sentence.split()

    unique_words = set(words)

    print(unique_words)

    print("-" * 60)

    # ==================================================
    # 13. Inventory Comparison
    # ==================================================

    print("\n13. Inventory Comparison")

    warehouse_a = {

        "Laptop",

        "Mouse",

        "Keyboard",

        "Monitor"

    }

    warehouse_b = {

        "Keyboard",

        "Mouse",

        "Printer",

        "Scanner"

    }

    print("Common Products")

    print(warehouse_a & warehouse_b)

    print()

    print("Only Warehouse A")

    print(warehouse_a - warehouse_b)

    print()

    print("Only Warehouse B")

    print(warehouse_b - warehouse_a)

    print("-" * 60)

    # ==================================================
    # 14. Website Visitors
    # ==================================================

    print("\n14. Unique Website Visitors")

    visitors = [

        "Alice",

        "Bob",

        "Alice",

        "Chris",

        "Bob",

        "David"

    ]

    print(set(visitors))

    print("-" * 60)

    # ==================================================
    # 15. Permission Checking
    # ==================================================

    print("\n15. Permission Checking")

    user_permissions = {

        "Read",

        "Write"

    }

    required_permissions = {

        "Read"

    }

    print(required_permissions <= user_permissions)

    print("-" * 60)

    # ==================================================
    # 16. Skill Matching
    # ==================================================

    print("\n16. Skill Matching")

    candidate = {

        "Python",

        "SQL",

        "Docker",

        "Git"

    }

    required = {

        "Python",

        "Docker"

    }

    print(candidate >= required)

    print("-" * 60)

    # ==================================================
    # 17. Find New Skills
    # ==================================================

    print("\n17. Newly Learned Skills")

    old_skills = {

        "Python",

        "SQL"

    }

    new_skills = {

        "Python",

        "SQL",

        "Docker",

        "AWS"

    }

    print(new_skills - old_skills)

    print("-" * 60)

    # ==================================================
    # 18. Merge Tags
    # ==================================================

    print("\n18. Merge Tags")

    tags1 = {

        "AI",

        "Python"

    }

    tags2 = {

        "Machine Learning",

        "Python"

    }

    print(tags1 | tags2)

    print("-" * 60)

    # ==================================================
    # 19. Compare Courses
    # ==================================================

    print("\n19. Compare Courses")

    python = {

        "Alice",

        "Bob",

        "Chris"

    }

    java = {

        "Bob",

        "Chris",

        "David"

    }

    print("Common")

    print(python & java)

    print()

    print("Different")

    print(python ^ java)

    print("-" * 60)

    # ==================================================
    # 20. Real-World Login Sessions
    # ==================================================

    print("\n20. Active User Sessions")

    active_users = {

        "Alice",

        "Bob",

        "Chris"

    }

    print("Before Logout")

    print(active_users)

    active_users.remove("Bob")

    print()

    print("After Logout")

    print(active_users)


if __name__ == "__main__":
    main()