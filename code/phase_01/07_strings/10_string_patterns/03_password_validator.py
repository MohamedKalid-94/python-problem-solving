"""
Topic: Password Validator

Problem:
Check minimum password length.
"""

password = input("Enter password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Password Too Short")