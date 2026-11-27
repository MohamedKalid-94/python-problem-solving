"""
=========================================================
Topic: Python Sets - Mathematical Operations
=========================================================

Concepts Covered

1. Union
2. Intersection
3. Difference
4. Symmetric Difference
5. issubset()
6. issuperset()
7. isdisjoint()
8. Real-World Examples
9. Time Complexity

"""

def main():

    # ==================================================
    # Sample Data
    # ==================================================

    set_a = {10, 20, 30, 40}
    set_b = {30, 40, 50, 60}

    print("=" * 60)
    print("Set A")
    print(set_a)

    print("\nSet B")
    print(set_b)


    # ==================================================
    # 1. Union
    # ==================================================

    print("\n" + "=" * 60)
    print("1. Union")
    print("=" * 60)

    union_set = set_a.union(set_b)

    print(union_set)

    # Using |
    print("\nUsing | operator")
    print(set_a | set_b)


    # ==================================================
    # 2. Intersection
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Intersection")
    print("=" * 60)

    intersection = set_a.intersection(set_b)

    print(intersection)

    # Using &
    print("\nUsing & operator")
    print(set_a & set_b)


    # ==================================================
    # 3. Difference
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Difference")
    print("=" * 60)

    print("A - B")

    print(set_a.difference(set_b))

    print()

    print("B - A")

    print(set_b.difference(set_a))

    # Using -
    print("\nUsing - operator")
    print(set_a - set_b)


    # ==================================================
    # 4. Symmetric Difference
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Symmetric Difference")
    print("=" * 60)

    symmetric = set_a.symmetric_difference(set_b)

    print(symmetric)

    # Using ^
    print("\nUsing ^ operator")
    print(set_a ^ set_b)


    # ==================================================
    # 5. Subset
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Subset")
    print("=" * 60)

    python_students = {"Alice", "Bob"}

    all_students = {"Alice", "Bob", "Chris", "David"}

    print(python_students.issubset(all_students))

    print(python_students <= all_students)


    # ==================================================
    # 6. Superset
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Superset")
    print("=" * 60)

    print(all_students.issuperset(python_students))

    print(all_students >= python_students)


    # ==================================================
    # 7. Disjoint Sets
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Disjoint Sets")
    print("=" * 60)

    team_a = {"Alice", "Bob"}

    team_b = {"Chris", "David"}

    print(team_a.isdisjoint(team_b))

    team_c = {"Bob", "Eva"}

    print(team_a.isdisjoint(team_c))


    # ==================================================
    # 8. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Common Skills")
    print("=" * 60)

    employee1 = {

        "Python",

        "SQL",

        "Docker",

        "Git"

    }

    employee2 = {

        "Python",

        "AWS",

        "Git",

        "Linux"

    }

    print("Employee 1 Skills")

    print(employee1)

    print()

    print("Employee 2 Skills")

    print(employee2)

    print()

    print("Common Skills")

    print(employee1 & employee2)

    print()

    print("All Skills")

    print(employee1 | employee2)

    print()

    print("Skills Employee 1 Only")

    print(employee1 - employee2)

    print()

    print("Unique Skills")

    print(employee1 ^ employee2)


    # ==================================================
    # 9. Time Complexity
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Time Complexity")
    print("=" * 60)

    print("Membership Test      : O(1) Average")

    print("Union                : O(len(A)+len(B))")

    print("Intersection         : O(min(len(A), len(B)))")

    print("Difference           : O(len(A))")

    print("Subset/Superset      : O(len(A))")

    print("Disjoint             : O(min(len(A), len(B)))")


if __name__ == "__main__":
    main()