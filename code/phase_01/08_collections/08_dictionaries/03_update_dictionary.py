"""
Topic: Update Dictionary

Problem:
Add and update dictionary values.
"""

student = {
    "name": "Kalid",
    "age": 25
}

student["age"] = 26

student["course"] = "Python"

print(student)

del student["age"]

print(student)