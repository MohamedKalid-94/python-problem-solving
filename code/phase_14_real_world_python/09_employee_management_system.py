"""
Phase 14 - Real World Python
Project 09 - Employee Management System
Employees are saved in employees.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text, ask_number

DATA_FILE = Path(__file__).with_name("employees.json")


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
        json.dump(employees, file, indent=4)


employees = load_data()


def find_employee(employee_id):
    """Return the employee with this ID, or None if there is no such employee."""
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None


def add_employee():
    employee_id = ask_text("ID: ")

    if find_employee(employee_id):
        print("ID already exists")
        return

    employees.append({
        "id": employee_id,
        "name": ask_text("Name: "),
        "department": ask_text("Department: "),
        "salary": ask_number("Salary: ", minimum=0.01)
    })
    save_data()
    print("Employee Added")


def view_employee():
    if not employees:
        print("No employees")
        return

    for employee in employees:
        print(employee)


def search_employee():
    employee = find_employee(ask_text("Employee ID: "))

    if employee:
        print(employee)
    else:
        print("Not Found")


def delete_employee():
    employee = find_employee(ask_text("Employee ID: "))

    if employee:
        employees.remove(employee)
        save_data()
        print("Deleted")
    else:
        print("Not Found")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()