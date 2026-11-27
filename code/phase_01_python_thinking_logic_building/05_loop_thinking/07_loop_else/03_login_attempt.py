"""
Topic: Loop else

Problem:
Search for the correct username.
"""

users = ["admin", "kalid", "guest"]

login_user = "kalid"

for user in users:

    if user == login_user:
        print("Login Successful")
        break

else:
    print("User Not Found")