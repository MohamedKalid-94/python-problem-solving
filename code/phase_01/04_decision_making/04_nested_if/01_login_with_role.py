"""
Topic: Nested if

Problem:
Login system with user role verification.

Flow:

Username Check
        |
        ↓
Password Check
        |
        ↓
Role Check
"""


username = "admin"

password = "admin123"

role = "manager"


if username == "admin":

    if password == "admin123":

        if role == "manager":
            print("Login successful - Manager Access")

        else:
            print("Limited Access")

    else:
        print("Wrong Password")

else:
    print("User Not Found")