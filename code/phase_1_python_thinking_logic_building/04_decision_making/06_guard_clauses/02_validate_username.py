"""
Topic: Guard Clauses

Problem:
Validate username.

Rules:
- Username should not be empty
- Username should have minimum length
"""


username = "kalid"


if username == "":
    print("Username cannot be empty")

elif len(username) < 5:
    print("Username is too short")

else:
    print("Username accepted")