"""
=========================================================
Topic : collections.defaultdict

Author: Mohamed Kalid

defaultdict is a dictionary subclass from the collections
module.

Normal Dictionary:

If key does not exist:
    KeyError

defaultdict:

If key does not exist:
    Creates a default value automatically


Common Uses:

1. Counting
2. Grouping data
3. Building nested dictionaries
4. Avoiding KeyError
5. Data aggregation

=========================================================
"""

from collections import defaultdict


def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Dictionary Problem
    # =====================================================

    separator("1. Normal Dictionary KeyError")

    student_marks = {}

    # student_marks["Math"] += 10

    print(
        "Normal dictionary gives KeyError "
        "when key does not exist"
    )


    # =====================================================
    # 2. Creating defaultdict
    # =====================================================

    separator("2. Creating defaultdict")

    numbers = defaultdict(int)

    print(numbers)

    print(numbers["missing"])

    print(numbers)


    # =====================================================
    # 3. defaultdict with int
    # Used for counting
    # =====================================================

    separator("3. defaultdict(int) - Counting")

    words = [

        "python",

        "java",

        "python",

        "python",

        "sql"

    ]

    word_count = defaultdict(int)


    for word in words:

        word_count[word] += 1


    print(word_count)



    # =====================================================
    # 4. defaultdict with list
    # Used for grouping
    # =====================================================

    separator("4. defaultdict(list) - Grouping")


    employees = [

        ("IT", "Alice"),

        ("HR", "Bob"),

        ("IT", "Chris"),

        ("Finance", "David"),

        ("HR", "Eva")

    ]


    department = defaultdict(list)


    for dept, employee in employees:

        department[dept].append(employee)


    print(department)


    print()

    print("IT Employees")

    print(department["IT"])



    # =====================================================
    # 5. defaultdict with set
    # Remove duplicates while grouping
    # =====================================================

    separator("5. defaultdict(set)")


    student_courses = [

        ("Alice", "Python"),

        ("Alice", "SQL"),

        ("Bob", "Python"),

        ("Alice", "Python")

    ]


    courses = defaultdict(set)


    for student, course in student_courses:

        courses[student].add(course)


    print(courses)



    # =====================================================
    # 6. defaultdict with string
    # =====================================================

    separator("6. defaultdict(str)")


    messages = defaultdict(str)


    print(messages["unknown"])



    # =====================================================
    # 7. Using lambda as default factory
    # =====================================================

    separator("7. defaultdict(lambda)")


    default_value = defaultdict(
        lambda: "Not Available"
    )


    print(default_value["name"])



    # =====================================================
    # 8. Nested defaultdict
    # =====================================================

    separator("8. Nested defaultdict")


    company = defaultdict(
        lambda: defaultdict(list)
    )


    company["Engineering"]["Backend"].append(
        "Python Developer"
    )


    company["Engineering"]["Frontend"].append(
        "React Developer"
    )


    company["HR"]["Recruitment"].append(
        "HR Manager"
    )


    print(company)



    # =====================================================
    # 9. Dictionary Conversion
    # =====================================================

    separator("9. Convert defaultdict to dict")


    data = defaultdict(int)


    data["Python"] = 10

    data["AI"] = 20


    normal_dict = dict(data)


    print(normal_dict)

    print(type(normal_dict))



    # =====================================================
    # 10. Group Words by Length
    # =====================================================

    separator("10. Group Words by Length")


    words = [

        "AI",

        "Python",

        "ML",

        "Data",

        "Cloud"

    ]


    grouped_words = defaultdict(list)


    for word in words:

        grouped_words[len(word)].append(word)


    print(grouped_words)



    # =====================================================
    # 11. Count Characters
    # =====================================================

    separator("11. Character Frequency")


    text = "programming"


    char_count = defaultdict(int)


    for char in text:

        char_count[char] += 1


    print(char_count)



    # =====================================================
    # 12. Product Category Example
    # =====================================================

    separator("12. Product Grouping")


    products = [

        ("Laptop", "Electronics"),

        ("Phone", "Electronics"),

        ("Shirt", "Fashion"),

        ("Shoes", "Fashion"),

        ("Book", "Education")

    ]


    category = defaultdict(list)


    for product, cat in products:

        category[cat].append(product)


    for key, value in category.items():

        print(key, ":", value)



    # =====================================================
    # 13. defaultdict vs dict
    # =====================================================

    separator("13. defaultdict vs dict")


    print(
        """
        Dictionary:

        data = {}

        if key missing:
            KeyError


        defaultdict:

        data = defaultdict(int)

        if key missing:
            creates default value

        """
    )



    # =====================================================
    # 14. Real World Example
    # =====================================================

    separator("14. Log Analyzer Example")


    logs = [

        ("ERROR", "Database failed"),

        ("INFO", "Server started"),

        ("ERROR", "Connection failed"),

        ("WARNING", "High memory")

    ]


    log_group = defaultdict(list)


    for level, message in logs:

        log_group[level].append(message)


    print(log_group)



if __name__ == "__main__":

    main()