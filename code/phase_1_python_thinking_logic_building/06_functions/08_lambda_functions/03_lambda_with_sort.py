"""
Topic: Lambda with sort()

Problem:
Sort tuples by age.
"""

students = [
    ("Rahul", 23),
    ("Kalid", 25),
    ("Arun", 21)
]

students.sort(key=lambda student: student[1])

print(students)