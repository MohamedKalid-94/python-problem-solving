"""
=========================================================
Topic : Iterators & Generators Real-World Problems

Project : Data Processing System

Concepts Covered:

1. Iterator Protocol
2. Custom Iterators
3. Generator Functions
4. yield Keyword
5. Generator Expressions
6. Lazy Evaluation
7. Real-World Data Processing

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Custom Iterator - Employee Records
# ---------------------------------------------------------

class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1
            return employee

        raise StopIteration


def custom_iterator_example():
    separator("1. Employee Iterator")

    employees = [
        "John",
        "Alice",
        "Kalid",
        "David"
    ]

    employee_iterator = EmployeeIterator(employees)

    for employee in employee_iterator:
        print("Employee:", employee)


# ---------------------------------------------------------
# Generator - Log File Reader
# ---------------------------------------------------------

def log_reader(logs):
    for log in logs:
        yield log


def log_reader_example():
    separator("2. Log File Generator")

    logs = [
        "INFO: Application Started",
        "WARNING: High Memory Usage",
        "ERROR: Database Connection Failed"
    ]

    for log in log_reader(logs):
        print(log)


# ---------------------------------------------------------
# Generator - Number Processing
# ---------------------------------------------------------

def even_number_generator(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def even_number_example():
    separator("3. Even Number Generator")

    numbers = range(1, 11)

    for number in even_number_generator(numbers):
        print(number)


# ---------------------------------------------------------
# Generator Expression - Data Filtering
# ---------------------------------------------------------

def generator_expression_example():
    separator("4. Generator Expression")

    transactions = [
        500,
        1500,
        2500,
        300,
        5000
    ]

    high_value_transactions = (
        amount
        for amount in transactions
        if amount > 1000
    )

    for amount in high_value_transactions:
        print("Transaction:", amount)


# ---------------------------------------------------------
# Lazy Evaluation - Large Dataset Processing
# ---------------------------------------------------------

def dataset_generator(size):
    for value in range(1, size + 1):
        yield value


def lazy_evaluation_example():
    separator("5. Lazy Dataset Processing")

    dataset = dataset_generator(1000000)

    print("First Value:", next(dataset))
    print("Second Value:", next(dataset))
    print("Third Value:", next(dataset))


# ---------------------------------------------------------
# API Pagination Generator
# ---------------------------------------------------------

def api_page_generator(total_pages):
    for page in range(1, total_pages + 1):
        print("Fetching API Page:", page)

        yield {
            "page": page,
            "data": f"Records from page {page}"
        }


def api_pagination_example():
    separator("6. API Pagination")

    pages = api_page_generator(3)

    for page in pages:
        print(page)


# ---------------------------------------------------------
# RAG Document Chunk Generator
# ---------------------------------------------------------

def document_chunk_generator(documents, chunk_size):
    for document in documents:
        words = document.split()

        for index in range(0, len(words), chunk_size):
            yield words[index:index + chunk_size]


def rag_chunking_example():
    separator("7. RAG Document Chunking")

    documents = [
        "Python is widely used in artificial intelligence applications",
        "Generators help process large documents efficiently"
    ]

    chunks = document_chunk_generator(documents, 3)

    for chunk in chunks:
        print("Chunk:", chunk)


# ---------------------------------------------------------
# Batch Processing Generator
# ---------------------------------------------------------

def batch_generator(data, batch_size):
    for index in range(0, len(data), batch_size):
        yield data[index:index + batch_size]


def batch_processing_example():
    separator("8. Batch Processing")

    records = list(range(1, 11))

    batches = batch_generator(records, 3)

    for batch in batches:
        print("Processing Batch:", batch)


# ---------------------------------------------------------
# Infinite Data Stream
# ---------------------------------------------------------

def sensor_data_stream():
    value = 1

    while True:
        yield f"Sensor Reading {value}"
        value += 1


def infinite_stream_example():
    separator("9. Sensor Data Stream")

    stream = sensor_data_stream()

    for _ in range(5):
        print(next(stream))


# ---------------------------------------------------------
# Real-World AI Data Loader
# ---------------------------------------------------------

def ai_dataset_loader(dataset):
    for item in dataset:
        yield {
            "input": item,
            "processed": item.upper()
        }


def ai_data_loader_example():
    separator("10. AI Dataset Loader")

    dataset = [
        "python",
        "machine learning",
        "generative ai"
    ]

    loader = ai_dataset_loader(dataset)

    for item in loader:
        print(item)


def main():
    custom_iterator_example()
    log_reader_example()
    even_number_example()
    generator_expression_example()
    lazy_evaluation_example()
    api_pagination_example()
    rag_chunking_example()
    batch_processing_example()
    infinite_stream_example()
    ai_data_loader_example()


if __name__ == "__main__":
    main()