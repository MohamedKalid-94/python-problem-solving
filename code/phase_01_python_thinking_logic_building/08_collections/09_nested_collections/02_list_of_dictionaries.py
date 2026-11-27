"""
Topic: List of Dictionaries

Problem:
Store multiple students.
"""

students = [
    {"name": "Alice", "age": 21},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 23}
]

for student in students:
    print(student["name"], student["age"])