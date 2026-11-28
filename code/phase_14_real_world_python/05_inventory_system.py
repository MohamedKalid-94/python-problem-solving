"""
Phase 14 - Real World Python
Project 05 - Inventory System
Products are saved in inventory.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text, ask_number, ask_int

DATA_FILE = Path(__file__).with_name("inventory.json")


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
        json.dump(inventory, file, indent=4)


inventory = load_data()


def add_product():
    pid = ask_text("Product ID: ")

    if pid in inventory:
        print("Product ID already exists")
        return

    inventory[pid] = {
        "name": ask_text("Name: "),
        "price": ask_number("Price: ", minimum=0.01),
        "quantity": ask_int("Quantity: ", minimum=0)
    }
    save_data()
    print("Product Added")


def view_products():
    if not inventory:
        print("No products")
        return

    for pid, product in inventory.items():
        print(pid, product["name"], product["price"], product["quantity"])


def update_stock():
    pid = ask_text("Product ID: ")

    if pid in inventory:
        inventory[pid]["quantity"] = ask_int("New Quantity: ", minimum=0)
        save_data()
        print("Stock Updated")
    else:
        print("Product Not Found")


def search_product():
    pid = ask_text("Product ID: ")
    print(inventory.get(pid, "Product Not Found"))


def delete_product():
    pid = ask_text("Product ID: ")

    if pid in inventory:
        del inventory[pid]
        save_data()
        print("Product Deleted")
    else:
        print("Product Not Found")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Update Stock\n4.Search\n5.Delete\n6.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()