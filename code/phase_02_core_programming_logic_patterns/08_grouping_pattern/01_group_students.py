"""
Topic: Group Students

Problem:
Group students by grade.
"""

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C")
]

groups = {}

for name, grade in students:
    groups.setdefault(grade, []).append(name)

print(groups)