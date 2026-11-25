"""
Topic: Email Validator

Problem:
Perform basic email validation.
"""

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")