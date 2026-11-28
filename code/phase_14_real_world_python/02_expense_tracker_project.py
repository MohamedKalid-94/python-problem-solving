"""
Phase 14 - Real World Python
Project 02 - Expense Tracker
Your expenses are saved in expenses.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text, ask_number

DATA_FILE = Path(__file__).with_name("expenses.json")


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
        json.dump(expenses, file, indent=4)


expenses = load_data()


def add_expense():
    # .title() so "food" and "Food" count as the same category
    category = ask_text("Enter category: ").title()
    amount = ask_number("Enter amount: ", minimum=0.01)

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_data()

    print("Expense Added")


def view_expenses():
    if not expenses:
        print("No expenses found")
        return

    print("\nExpense List")

    for index, expense in enumerate(expenses, 1):
        print(index, expense["category"], expense["amount"])


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense:", round(total, 2))


def category_summary():
    if not expenses:
        print("No expenses found")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount

    print("\nCategory Summary")

    for category, amount in summary.items():
        print(category, round(amount, 2))


def main():
    while True:
        print(
            """
Expense Tracker

1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Exit
"""
        )

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Expense Tracker Closed")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()