"""
Topic: Decision Pattern - Validation

Problem:
Validate user registration data.

Rules:

Name should exist
Age should be valid
"""


name = "Kalid"

age = 25


if name == "":
    print("Name is required")

elif age < 18:
    print("Age should be above 18")

else:
    print("Registration successful")