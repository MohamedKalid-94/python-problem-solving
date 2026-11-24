"""
Topic: Mutable vs Immutable

Concept:
Dictionary values can be updated.

Mutable Object:
Dictionary
"""

employee = {
    "name": "Kalid",
    "salary": 50000
}

print("Before Update")
print(employee)


employee["salary"] = 60000


print()

print("After Update")
print(employee)