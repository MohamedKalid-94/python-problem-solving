"""
Topic: Membership Operators

Concept:
Check username availability.
"""


existing_users = [
    "admin",
    "kalid",
    "john"
]


new_username = "kalid"


print("Username Check")
print("--------------")


print(
    "Username Already Exists:",
    new_username in existing_users
)
