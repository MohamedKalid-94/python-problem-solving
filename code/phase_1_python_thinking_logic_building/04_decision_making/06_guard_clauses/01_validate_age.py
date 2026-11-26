"""
Topic: Guard Clauses

Problem:
Validate user age before allowing access.

Concept:
Handle invalid cases first.
"""


age = 15


if age < 18:
    print("Access denied: Age must be 18 or above")

else:
    print("Access granted")