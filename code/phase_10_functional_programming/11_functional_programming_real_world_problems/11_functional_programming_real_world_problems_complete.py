"""
=========================================================
Topic : Functional Programming - Real-World Problems

Covered:

1. Employee Salary Processing
2. Student Result Analysis
3. E-Commerce Order Processing
4. API Response Processing
5. Log File Analysis
6. AI Dataset Preprocessing
7. RAG Document Processing Pipeline

Concepts Used:
- map()
- filter()
- reduce()
- zip()
- enumerate()
- any()
- all()
- sorted()
- key functions
- Higher-order functions

=========================================================
"""

from functools import reduce


def separator(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------
# 1. Employee Salary Processing
# ---------------------------------------------------------

def employee_salary_processing():
    separator("1. Employee Salary Processing")

    employees = [
        {"name": "John", "salary": 45000},
        {"name": "Alice", "salary": 62000},
        {"name": "David", "salary": 58000},
        {"name": "Sara", "salary": 71000}
    ]

    increased_salary = list(
        map(
            lambda employee: {
                "name": employee["name"],
                "salary": round(employee["salary"] * 1.10)
            },
            employees
        )
    )

    for employee in increased_salary:
        print(employee)


# ---------------------------------------------------------
# 2. Student Result Analysis
# ---------------------------------------------------------

def student_result_analysis():
    separator("2. Student Result Analysis")

    students = [
        {"name": "John", "marks": 85},
        {"name": "Alice", "marks": 42},
        {"name": "David", "marks": 67},
        {"name": "Sara", "marks": 95},
        {"name": "Kalid", "marks": 38}
    ]

    passed_students = list(
        filter(
            lambda student: student["marks"] >= 50,
            students
        )
    )

    ranking = sorted(
        passed_students,
        key=lambda student: student["marks"],
        reverse=True
    )

    for rank, student in enumerate(ranking, start=1):
        print(f"{rank}. {student['name']} - {student['marks']}")


# ---------------------------------------------------------
# 3. E-Commerce Order Processing
# ---------------------------------------------------------

def ecommerce_order_processing():
    separator("3. E-Commerce Order Processing")

    orders = [
        {"id": 101, "amount": 1200},
        {"id": 102, "amount": 450},
        {"id": 103, "amount": 3500},
        {"id": 104, "amount": 800}
    ]

    valid_orders = list(
        filter(
            lambda order: order["amount"] >= 1000,
            orders
        )
    )

    total_sales = reduce(
        lambda total, order: total + order["amount"],
        valid_orders,
        0
    )

    print("Valid Orders")

    for order in valid_orders:
        print(order)

    print("Total Sales:", total_sales)


# ---------------------------------------------------------
# 4. API Response Processing
# ---------------------------------------------------------

def api_response_processing():
    separator("4. API Response Processing")

    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"},
        {"id": 3, "name": "David"}
    ]

    user_names = list(
        map(
            lambda user: user["name"].upper(),
            users
        )
    )

    print(user_names)


# ---------------------------------------------------------
# 5. Log File Analysis
# ---------------------------------------------------------

def log_file_analysis():
    separator("5. Log File Analysis")

    logs = [
        "INFO: Login Successful",
        "ERROR: Database Connection Failed",
        "INFO: File Uploaded",
        "WARNING: Disk Usage High",
        "ERROR: Timeout"
    ]

    errors = list(
        filter(
            lambda log: log.startswith("ERROR"),
            logs
        )
    )

    print("Errors Found:", len(errors))

    for error in errors:
        print(error)


# ---------------------------------------------------------
# 6. AI Dataset Preprocessing
# ---------------------------------------------------------

def ai_dataset_preprocessing():
    separator("6. AI Dataset Preprocessing")

    dataset = [
        "python",
        "machine learning",
        "artificial intelligence",
        "rag",
        "langchain"
    ]

    processed_dataset = list(
        map(
            lambda text: text.title(),
            dataset
        )
    )

    print(processed_dataset)


# ---------------------------------------------------------
# 7. RAG Document Processing Pipeline
# ---------------------------------------------------------

def rag_document_processing():
    separator("7. RAG Document Processing Pipeline")

    documents = [
        "Introduction to Python",
        "Machine Learning Basics",
        "Vector Databases",
        "Large Language Models",
        "Agentic AI Systems"
    ]

    document_ids = range(1, len(documents) + 1)

    indexed_documents = list(
        zip(document_ids, documents)
    )

    sorted_documents = sorted(
        indexed_documents,
        key=lambda document: len(document[1])
    )

    print("Indexed Documents")

    for document_id, title in sorted_documents:
        print(f"{document_id}: {title}")


# ---------------------------------------------------------
# Bonus Example
# ---------------------------------------------------------

def functional_pipeline():
    separator("Bonus: Functional Programming Pipeline")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = list(
        map(
            lambda number: number ** 2,
            filter(
                lambda number: number % 2 == 0,
                numbers
            )
        )
    )

    print("Original Numbers :", numbers)
    print("Even Squares     :", result)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():
    employee_salary_processing()
    student_result_analysis()
    ecommerce_order_processing()
    api_response_processing()
    log_file_analysis()
    ai_dataset_preprocessing()
    rag_document_processing()
    functional_pipeline()


if __name__ == "__main__":
    main()