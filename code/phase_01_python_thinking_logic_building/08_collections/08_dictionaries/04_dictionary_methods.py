"""
Topic: Dictionary Methods

Problem:
Use common dictionary methods.
"""

student = {
    "name": "Kalid",
    "age": 25,
    "course": "Python"
}

print(student.keys())
print(student.values())
print(student.items())

print(student.pop("age"))

print(student)

student.clear()

print(student)