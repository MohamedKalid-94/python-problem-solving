"""
=========================================================
Topic : File Append Operations

Author: Mohamed Kalid

Covered:

1. Append mode
2. Add new records
3. Application logging
4. User activity history
5. Transaction history
6. Error log handling
7. AI application logging example

File modes:

r  -> Read
w  -> Write (overwrite)
a  -> Append (add content)
x  -> Create new file

=========================================================
"""


from datetime import datetime
from pathlib import Path

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def create_initial_file():
    separator("1. Create Initial File")
    file_name = "users.txt"
    with open(file_name, "w") as file:
        file.write("Alice\n")
        file.write("Bob\n")
    print("Initial users created")

def append_new_record():
    separator("2. Append New Record")
    file_name = "users.txt"
    new_users = [
        "Chris",
        "David"
    ]

    with open(file_name, "a") as file:
        for user in new_users:
            file.write(user + "\n")
    print("New users added")

def read_file():
    separator("3. Read Updated File")
    with open("users.txt", "r") as file:
        content = file.read()
    print(content)

def application_logger():
    separator("4. Application Logger")
    log_file = "application.log"
    messages = [
        "User Login Successful",
        "File Uploaded",
        "Database Connected"
    ]

    with open(log_file, "a") as file:
        for message in messages:
            timestamp = datetime.now()
            file.write(
                f"{timestamp} - {message}\n"
            )
    print("Application logs updated")

def user_activity_history():
    separator("5. User Activity History")
    history_file = "activity.log"
    activities = [
        "Opened Dashboard",
        "Downloaded Report",
        "Logged Out"
    ]

    with open(history_file, "a") as file:
        for activity in activities:
            file.write(
                activity + "\n"
            )
    print("User history saved")

def transaction_history():
    separator("6. Transaction History")
    transaction_file = "transactions.txt"
    transactions = [
        "TX001,1000,Success",
        "TX002,2500,Success",
        "TX003,500,Failed"
    ]

    with open(transaction_file, "a") as file:
        for transaction in transactions:
            file.write(
                transaction + "\n"
            )
    print("Transactions recorded")

def count_log_errors():
    separator("7. Error Log Analyzer")
    log_file = "error.log"
    errors = [
        "ERROR Database Connection Failed",
        "INFO Server Started",
        "ERROR API Timeout",
        "WARNING Memory Low"
    ]

    with open(log_file, "a") as file:
        for error in errors:
            file.write(error + "\n")
    error_count = 0


    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
    print(
        "Total Errors:",
        error_count
    )



def append_json_style_data():
    separator("8. Append AI Metadata")
    metadata_file = "metadata.txt"
    documents = [
        "Python Document",
        "AI Document",
        "RAG Document"
    ]
    with open(metadata_file, "a") as file:
        for document in documents:
            file.write(
                document + "\n"
            )
    print("Metadata stored")


def safe_append_with_pathlib():
    separator("9. File Check Before Append")
    file_path = Path("report.txt")
    if not file_path.exists():
        file_path.touch()
    with open(file_path, "a") as file:
        file.write(
            "New report generated\n"
        )
    print(
        "Report updated"
    )

def main():
    create_initial_file()
    append_new_record()
    read_file()
    application_logger()
    user_activity_history()
    transaction_history()
    count_log_errors()
    append_json_style_data()
    safe_append_with_pathlib()

if __name__ == "__main__":
    main()