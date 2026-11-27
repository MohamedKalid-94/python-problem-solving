"""
Topic: Contact Book

Problem:
Store names and phone numbers.
"""

contacts = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9988776655"
}

name = input("Enter name: ")

print(contacts.get(name, "Contact Not Found"))