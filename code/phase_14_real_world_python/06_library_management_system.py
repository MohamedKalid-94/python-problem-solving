"""
Phase 14 - Real World Python
Project 06 - Library Management System
Books are saved in books.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text

DATA_FILE = Path(__file__).with_name("books.json")


def load_data():
    """Read saved data from the JSON file (empty list if there is none)."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Data file is damaged. Starting empty.")
    return []


def save_data():
    """Write the current data to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


books = load_data()


def find_book(book_id):
    """Return the book with this ID, or None if there is no such book."""
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def add_book():
    book_id = ask_text("Book ID: ")

    if find_book(book_id):
        print("Book ID already exists")
        return

    books.append({
        "id": book_id,
        "title": ask_text("Title: "),
        "author": ask_text("Author: "),
        "issued": False
    })
    save_data()
    print("Book Added")


def view_books():
    if not books:
        print("No books")
        return

    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(book["id"], book["title"], book["author"], status)


def issue_book():
    book = find_book(ask_text("Book ID: "))

    if book is None:
        print("Book Not Found")
    elif book["issued"]:
        print("Book is already issued")
    else:
        book["issued"] = True
        save_data()
        print("Book Issued")


def return_book():
    book = find_book(ask_text("Book ID: "))

    if book is None:
        print("Book Not Found")
    elif not book["issued"]:
        print("Book was not issued")
    else:
        book["issued"] = False
        save_data()
        print("Book Returned")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Issue\n4.Return\n5.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()