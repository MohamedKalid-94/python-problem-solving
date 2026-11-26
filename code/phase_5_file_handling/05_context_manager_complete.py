"""
=========================================================
Topic : Context Manager in Python

Author: Mohamed Kalid

Covered:

1. Understanding context manager
2. File handling with with statement
3. Automatic resource cleanup
4. Exception handling
5. Custom context manager
6. Timer context manager
7. AI application logging example

=========================================================
"""

from datetime import datetime
import time

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def normal_file_handling():
    separator("1. Normal File Handling")
    file = open(
        "normal_file.txt",
        "w"
    )
    file.write(
        "Learning Python File Handling"
    )
    file.close()
    print(
        "File closed manually"
    )

def context_manager_file_handling():
    separator("2. Context Manager File Handling")
    with open(
        "context_file.txt",
        "w"
    ) as file:
        file.write(
            "Using Context Manager"
        )
    print(
        "File automatically closed"
    )

def exception_safe_file_handling():
    separator("3. Exception Safe File Handling")

    try:
        with open(
            "error_file.txt",
            "w"
        ) as file:
            file.write(
                "Safe writing"
            )
            raise Exception(
                "Testing exception"
            )

    except Exception as error:
        print(
            error
        )
    print(
        "Resource released automatically"
    )

class FileLogger:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(
            self.file_name,
            "a"
        )
        self.file.write(
            "\n--- Log Started ---\n"
        )
        return self.file

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):

        self.file.write(
            "--- Log Completed ---\n"
        )
        self.file.close()

        print(
            "Logger closed"
        )

def custom_file_context_manager():
    separator("4. Custom File Context Manager")
    with FileLogger(
        "application.log"
    ) as logger:
        logger.write(
            "User logged in\n"
        )
        logger.write(
            "Document uploaded\n"
        )

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback
    ):

        self.end = time.time()
        print(
            "Execution Time:",
            self.end - self.start,
            "seconds"
        )

def timer_context_manager():
    separator("5. Timer Context Manager")
    with Timer():
        total = 0
        for number in range(1000000):
            total += number

    print(
        "Calculation completed"
    )

def transaction_context_manager():
    separator("6. Transaction Pattern")

    class Transaction:
        def __enter__(self):
            print(
                "Transaction Started"
            )
            return self

        def __exit__(
            self,
            exception_type,
            exception_value,
            traceback
        ):

            if exception_type:
                print(
                    "Transaction Failed - Rollback"
                )
            else:
                print(
                    "Transaction Completed"
                )

    with Transaction():
        print(
            "Processing data..."
        )

def ai_logging_context_manager():
    separator("7. AI Application Logging")

    class AIRequestLogger:
        def __enter__(self):
            self.file = open(
                "ai_requests.log",
                "a"
            )
            self.file.write(
                f"\nRequest Started: {datetime.now()}\n"
            )
            return self.file

        def __exit__(
            self,
            exception_type,
            exception_value,
            traceback
        ):
            self.file.write(
                f"Request Completed: {datetime.now()}\n"
            )
            self.file.close()

    with AIRequestLogger() as log:
        log.write(
            "User Query: Explain RAG\n"
        )
        log.write(
            "LLM Response Generated\n"
        )
    print(
        "AI trace saved"
    )

def main():
    normal_file_handling()
    context_manager_file_handling()
    exception_safe_file_handling()
    custom_file_context_manager()
    timer_context_manager()
    transaction_context_manager()
    ai_logging_context_manager()

if __name__ == "__main__":
    main()