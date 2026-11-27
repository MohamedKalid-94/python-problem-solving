"""
=========================================================
Topic : CSV File Processing in Python

Author: Mohamed Kalid

Covered:

1. Create CSV files
2. Read CSV files
3. Write CSV files
4. DictReader
5. DictWriter
6. Filter CSV data
7. CSV analytics
8. Data cleaning
9. AI dataset preprocessing example

=========================================================
"""

import csv
from pathlib import Path
from collections import Counter

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def create_employee_csv():
    separator("1. Create Employee CSV")
    file_name = "employees.csv"
    employees = [
        ["id", "name", "role", "salary"],
        [1, "Alice", "Developer", 90000],
        [2, "Bob", "Tester", 50000],
        [3, "Chris", "Developer", 80000],
        [4, "David", "Manager", 100000]
    ]

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employees)
    print("Employee CSV created")

def read_csv_file():
    separator("2. Read CSV File")
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def read_csv_using_dictreader():
    separator("3. Read CSV Using DictReader")
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for employee in reader:
            print(
                employee["name"],
                employee["role"]
            )

def write_csv_using_dictwriter():
    separator("4. Write CSV Using DictWriter")
    file_name = "projects.csv"
    projects = [
        {
            "id": 1,
            "project": "AI Assistant",
            "status": "Completed"
        },
        {
            "id": 2,
            "project": "RAG System",
            "status": "In Progress"
        }
    ]

    with open(
        file_name,
        "w",
        newline=""
    ) as file:
        field_names = [
            "id",
            "project",
            "status"
        ]
        writer = csv.DictWriter(
            file,
            fieldnames=field_names
        )
        writer.writeheader()
        writer.writerows(projects)
    print("Projects CSV created")

def employee_salary_analysis():
    separator("5. Employee Salary Analysis")
    total_salary = 0
    employee_count = 0
    highest_salary = 0
    highest_employee = ""

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for employee in reader:
            salary = int(
                employee["salary"]
            )
            total_salary += salary
            employee_count += 1

            if salary > highest_salary:
                highest_salary = salary
                highest_employee = employee["name"]

    average_salary = (
        total_salary / employee_count
    )

    print(
        "Average Salary:",
        average_salary
    )

    print(
        "Highest Salary Employee:",
        highest_employee
    )


def role_counter():
    separator("6. Role Frequency Analysis")
    roles = []

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            roles.append(
                employee["role"]
            )

    role_count = Counter(roles)
    print(role_count)



def filter_csv_data():
    separator("7. Filter CSV Data")
    developers = []
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for employee in reader:
            if employee["role"] == "Developer":
                developers.append(employee)

    with open(
        "developers.csv",
        "w",
        newline=""
    ) as file:
        field_names = [
            "id",
            "name",
            "role",
            "salary"
        ]
        writer = csv.DictWriter(
            file,
            fieldnames=field_names
        )
        writer.writeheader()
        writer.writerows(developers)

    print(
        "Developer CSV created"
    )

def remove_duplicate_records():
    separator("8. Remove Duplicate Records")
    records = [
        ["Alice", "Developer"],
        ["Bob", "Tester"],
        ["Alice", "Developer"]
    ]
    unique_records = []
    seen = set()
    for record in records:
        record_tuple = tuple(record)
        if record_tuple not in seen:
            seen.add(record_tuple)
            unique_records.append(record)
    print(unique_records)

def csv_data_cleaning():
    separator("9. CSV Data Cleaning")

    raw_users = [
        {
            "name": "Alice",
            "email": "alice@gmail.com"
        },
        {
            "name": "",
            "email": "invalid"
        },
        {
            "name": "Bob",
            "email": "bob@gmail.com"
        }
    ]


    clean_users = [
        user
        for user in raw_users
        if user["name"]
        and "@gmail.com" in user["email"]
    ]
    print(clean_users)

def ai_dataset_preprocessing():
    separator("10. AI Dataset Processing Example")
    documents = [
        {
            "id": 1,
            "text": "Python programming language"
        },
        {
            "id": 2,
            "text": "AI and Machine Learning"
        },
        {
            "id": 3,
            "text": ""
        }
    ]


    processed_documents = [
        {
            "id": doc["id"],
            "length": len(doc["text"])
        }
        for doc in documents
        if doc["text"]
    ]
    print(processed_documents)

def pathlib_csv_operations():
    separator("11. CSV File Information")
    file = Path("employees.csv")
    if file.exists():
        print(
            "File:",
            file.name
        )
        print(
            "Size:",
            file.stat().st_size,
            "bytes"
        )

def main():
    create_employee_csv()
    read_csv_file()
    read_csv_using_dictreader()
    write_csv_using_dictwriter()
    employee_salary_analysis()
    role_counter()
    filter_csv_data()
    remove_duplicate_records()
    csv_data_cleaning()
    ai_dataset_preprocessing()
    pathlib_csv_operations()

if __name__ == "__main__":
    main()