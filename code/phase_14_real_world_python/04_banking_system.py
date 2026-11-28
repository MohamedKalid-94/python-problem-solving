"""
Phase 14 - Real World Python
Project 04 - Banking System
Accounts are saved in accounts.json (next to this file).
Note: floats are fine for learning; real money code uses Decimal or whole cents.
"""

import json
from pathlib import Path

from helpers import ask_text, ask_number

DATA_FILE = Path(__file__).with_name("accounts.json")


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
        json.dump(accounts, file, indent=4)


accounts = load_data()


def create_account():
    acc = ask_text("Account No: ")

    if acc in accounts:
        print("Account already exists")
        return

    name = ask_text("Name: ")
    balance = ask_number("Initial Balance: ", minimum=0)

    accounts[acc] = {"name": name, "balance": balance}
    save_data()
    print("Account Created")


def deposit():
    acc = ask_text("Account No: ")

    if acc not in accounts:
        print("Account Not Found")
        return

    amount = ask_number("Deposit Amount: ", minimum=0.01)
    accounts[acc]["balance"] += amount
    save_data()
    print("Deposit Successful")


def withdraw():
    acc = ask_text("Account No: ")

    if acc not in accounts:
        print("Account Not Found")
        return

    amount = ask_number("Withdraw Amount: ", minimum=0.01)

    if accounts[acc]["balance"] >= amount:
        accounts[acc]["balance"] -= amount
        save_data()
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")


def check_balance():
    acc = ask_text("Account No: ")

    if acc in accounts:
        print(accounts[acc]["name"], "-", round(accounts[acc]["balance"], 2))
    else:
        print("Account Not Found")


def main():
    while True:
        print("\n1.Create\n2.Deposit\n3.Withdraw\n4.Balance\n5.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()