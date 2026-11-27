"""
Topic: Logical Operators

Concept:
Use 'and' operator to validate multiple conditions.

Real-world Example:
Login system validation.
"""

username = "admin"

password = "admin123"


valid_username = username == "admin"

valid_password = password == "admin123"


login_success = valid_username and valid_password


print("Login Validation")
print("----------------")

print("Username Correct:", valid_username)

print("Password Correct:", valid_password)

print("Login Success:", login_success)