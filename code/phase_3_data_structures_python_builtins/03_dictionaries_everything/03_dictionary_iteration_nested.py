"""
=========================================================
Topic: Dictionary Iteration and Nested Dictionaries
=========================================================

Concepts Covered:
1. Iterating Over Keys
2. Iterating Over Values
3. Iterating Over Key-Value Pairs
4. Nested Dictionaries
5. Dictionary of Lists
6. List of Dictionaries
7. Real-World Examples
8. Nested Loop Traversal
9. Practical Examples

"""

def main():

    # ==================================================
    # 1. Iterating Through Keys
    # ==================================================

    print("=" * 60)
    print("1. Iterating Through Keys")
    print("=" * 60)

    student = {
        "id": 101,
        "name": "Alice",
        "age": 22,
        "course": "Python"
    }

    print("Dictionary")
    print(student)

    print("\nUsing for loop")

    for key in student:
        print(key)

    print("\nUsing keys()")

    for key in student.keys():
        print(key)


    # ==================================================
    # 2. Iterating Through Values
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Iterating Through Values")
    print("=" * 60)

    for value in student.values():
        print(value)


    # ==================================================
    # 3. Iterating Through Items
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Iterating Through Key-Value Pairs")
    print("=" * 60)

    for key, value in student.items():

        print(f"{key} : {value}")


    # ==================================================
    # 4. Nested Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Nested Dictionary")
    print("=" * 60)

    students = {

        101: {
            "name": "Alice",
            "age": 22,
            "course": "Python"
        },

        102: {
            "name": "Bob",
            "age": 23,
            "course": "Java"
        },

        103: {
            "name": "Chris",
            "age": 21,
            "course": "AI"
        }

    }

    print(students)

    print("\nAccess Individual Value")

    print(students[101]["name"])

    print(students[102]["course"])


    # ==================================================
    # 5. Iterating Nested Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Iterating Nested Dictionary")
    print("=" * 60)

    for student_id, details in students.items():

        print(f"\nStudent ID : {student_id}")

        for key, value in details.items():

            print(f"{key:<10} : {value}")


    # ==================================================
    # 6. Dictionary of Lists
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Dictionary of Lists")
    print("=" * 60)

    classroom = {

        "Python": [

            "Alice",

            "Bob",

            "David"

        ],

        "AI": [

            "Chris",

            "Eva"

        ]

    }

    print(classroom)

    print()

    for course, students in classroom.items():

        print(course)

        for student in students:

            print("  ", student)


    # ==================================================
    # 7. List of Dictionaries
    # ==================================================

    print("\n" + "=" * 60)
    print("7. List of Dictionaries")
    print("=" * 60)

    employees = [

        {
            "id": 101,
            "name": "Alice",
            "role": "Developer"
        },

        {
            "id": 102,
            "name": "Bob",
            "role": "Tester"
        },

        {
            "id": 103,
            "name": "Chris",
            "role": "Manager"
        }

    ]

    for employee in employees:

        print(employee)

    print("\nEmployee Details\n")

    for employee in employees:

        print(f"ID   : {employee['id']}")
        print(f"Name : {employee['name']}")
        print(f"Role : {employee['role']}")
        print("-" * 25)


    # ==================================================
    # 8. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Company Database")
    print("=" * 60)

    company = {

        "HR": {

            "Manager": "Alice",

            "Employees": 15

        },

        "IT": {

            "Manager": "Bob",

            "Employees": 45

        },

        "Finance": {

            "Manager": "Chris",

            "Employees": 20

        }

    }

    for department, details in company.items():

        print(f"\nDepartment : {department}")

        for key, value in details.items():

            print(f"{key:<10} : {value}")


    # ==================================================
    # 9. Nested Dictionary Lookup
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Nested Lookup")
    print("=" * 60)

    print(company["IT"]["Manager"])

    print(company["Finance"]["Employees"])


    # ==================================================
    # 10. Dictionary Inside Dictionary Inside Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Multiple Nested Levels")
    print("=" * 60)

    data = {

        "India": {

            "Tamil Nadu": {

                "Capital": "Chennai",

                "Language": "Tamil"

            }

        }

    }

    print(data["India"]["Tamil Nadu"]["Capital"])

    print(data["India"]["Tamil Nadu"]["Language"])


if __name__ == "__main__":
    main()