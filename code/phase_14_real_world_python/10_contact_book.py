"""
Phase 14 - Real World Python
Project 10 - Contact Book
Contacts are saved in contacts.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_data():
    """Read saved data from the JSON file (empty dictionary if there is none)."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Data file is damaged. Starting empty.")
    return {}


def save_data():
    """Write the current data to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


contacts = load_data()


def ask_phone(prompt):
    """Keep asking until the phone number has 7 to 15 digits."""
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        print("Phone must be 7 to 15 digits (numbers only).")


def ask_email(prompt):
    """Keep asking until the email looks valid (a simple check, not a full one)."""
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email.split("@")[-1] and " " not in email:
            return email
        print("Please enter a valid email like name@example.com")


def add_contact():
    # .title() so "kalid" and "Kalid" are the same contact
    name = ask_text("Name: ").title()

    if name in contacts:
        print("Contact already exists")
        return

    contacts[name] = {
        "phone": ask_phone("Phone: "),
        "email": ask_email("Email: ")
    }
    save_data()
    print("Contact Added")


def view_contacts():
    if not contacts:
        print("No contacts")
        return

    for name, details in contacts.items():
        print(name, details["phone"], details["email"])


def search_contact():
    name = ask_text("Name: ").title()
    print(contacts.get(name, "Not Found"))


def delete_contact():
    name = ask_text("Name: ").title()

    if name in contacts:
        del contacts[name]
        save_data()
        print("Deleted")
    else:
        print("Not Found")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()