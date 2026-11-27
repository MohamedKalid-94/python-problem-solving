"""
Topic: break Statement

Problem:
Stop checking after correct password.
"""

passwords = ["abc", "1234", "admin"]

correct_password = "1234"

for password in passwords:

    if password == correct_password:
        print("Login Successful")
        break

    print("Checking:", password)