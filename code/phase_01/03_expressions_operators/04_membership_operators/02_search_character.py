"""
Topic: Membership Operators

Concept:
Search characters inside a string.
"""


message = "Python Programming"


character = "P"


print("Character Search")
print("----------------")


print("Character Exists:", character in message)

print("Character Missing:", character not in message)