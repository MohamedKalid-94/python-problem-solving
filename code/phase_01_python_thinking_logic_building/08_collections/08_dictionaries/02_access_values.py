"""
Topic: Access Dictionary Values

Problem:
Access values using keys.
"""

student = {
    "name": "Kalid",
    "age": 25,
    "course": "Python"
}

print(student["name"])
print(student["age"])

print(student.get("course"))
print(student.get("city", "Not Found"))