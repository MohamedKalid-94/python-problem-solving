"""
Phase 14 - Real World Python
Project 03 - Student Management System
Students are saved in students.json (next to this file).
"""

import json
from pathlib import Path

from helpers import ask_text, ask_number, ask_int

DATA_FILE = Path(__file__).with_name("students.json")


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
        json.dump(students, file, indent=4)


students = load_data()


def find_student(student_id):
    """Return the student with this ID, or None if there is no such student."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    student_id = ask_text("ID: ")

    if find_student(student_id):
        print("ID already exists")
        return

    student = {
        "id": student_id,
        "name": ask_text("Name: "),
        "age": ask_int("Age: ", 1, 120),
        "course": ask_text("Course: "),
        "marks": ask_number("Marks (0-100): ", 0, 100),
    }

    students.append(student)
    save_data()
    print("Student Added")


def view_students():
    if not students:
        print("No Records")
        return

    for student in students:
        print(student)


def search_student():
    student = find_student(ask_text("Enter ID: "))

    if student:
        print(student)
    else:
        print("Student Not Found")


def update_student():
    student = find_student(ask_text("Enter ID: "))

    if student:
        student["marks"] = ask_number("New Marks (0-100): ", 0, 100)
        save_data()
        print("Updated")
    else:
        print("Student Not Found")


def delete_student():
    student = find_student(ask_text("Enter ID: "))

    if student:
        students.remove(student)
        save_data()
        print("Deleted")
    else:
        print("Student Not Found")


def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()