"""
Topic: Identity Operators

Concept:
Check same object reference.
"""


student_details = {
    "name": "Kalid",
    "age": 28
}


student_copy = student_details


print("Same Object Check")
print("-----------------")


print(student_details is student_copy)