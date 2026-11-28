"""
Phase 14 - Real World Python
Project 08 - Password Manager
LEARNING PROJECT ONLY. Passwords are kept in memory and are NOT saved.
Saving real passwords in a plain text file is unsafe. Real tools encrypt them.
"""

from getpass import getpass

from helpers import ask_text

passwords = {}


def add_password():
    site = ask_text("Website: ")

    if site in passwords:
        print("Website already saved")
        return

    passwords[site] = {
        "username": ask_text("Username: "),
        "password": getpass("Password (hidden): ")      # does not show what you type
    }
    print("Password Saved")


def view_passwords():
    if not passwords:
        print("No passwords saved")
        return

    for site, details in passwords.items():
        print(site, details["username"], "********")    # never print real passwords in a list


def search_password():
    site = ask_text("Website: ")
    details = passwords.get(site)

    if details is None:
        print("Not Found")
    else:
        print(site, details["username"], details["password"])


def delete_password():
    site = ask_text("Website: ")

    if site in passwords:
        del passwords[site]
        print("Deleted")
    else:
        print("Not Found")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()