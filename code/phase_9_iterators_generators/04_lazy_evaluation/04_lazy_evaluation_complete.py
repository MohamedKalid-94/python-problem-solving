"""
=========================================================
Topic : Lazy Evaluation in Python

Covered:

1. Eager vs Lazy Evaluation
2. Lazy Execution
3. Generators and Lazy Evaluation
4. Infinite Data Processing
5. Large Data Processing
6. Pipeline Processing
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Eager Evaluation
# ---------------------------------------------------------

def eager_evaluation_example():
    separator("1. Eager Evaluation")

    numbers = [number * 2 for number in range(5)]

    print("All values created immediately:")
    print(numbers)


# ---------------------------------------------------------
# Lazy Evaluation
# ---------------------------------------------------------

def lazy_numbers():
    for number in range(5):
        print("Generating:", number)
        yield number * 2


def lazy_evaluation_example():
    separator("2. Lazy Evaluation")

    numbers = lazy_numbers()

    print("Generator created.")

    print(next(numbers))
    print(next(numbers))


# ---------------------------------------------------------
# Generator Pipeline
# ---------------------------------------------------------

def read_numbers():
    for number in range(1, 11):
        yield number


def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square_numbers(numbers):
    for number in numbers:
        yield number * number


def pipeline_example():
    separator("3. Generator Pipeline")

    numbers = read_numbers()

    even_numbers = filter_even(numbers)

    squared_numbers = square_numbers(even_numbers)

    for number in squared_numbers:
        print(number)


# ---------------------------------------------------------
# Infinite Data Processing
# ---------------------------------------------------------

def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


def infinite_processing_example():
    separator("4. Infinite Data Processing")

    numbers = infinite_numbers()

    for _ in range(5):
        print(next(numbers))


# ---------------------------------------------------------
# Large File Processing
# ---------------------------------------------------------

def read_large_file():
    data = [
        "Python",
        "Machine Learning",
        "Generative AI",
        "RAG",
        "Agents"
    ]

    for item in data:
        yield item


def large_file_processing_example():
    separator("5. Large File Processing")

    for line in read_large_file():
        print("Processing:", line)


# ---------------------------------------------------------
# Lazy API Pagination
# ---------------------------------------------------------

def fetch_pages(total_pages):
    for page in range(1, total_pages + 1):
        print("Fetching page:", page)
        yield f"Data from page {page}"


def pagination_example():
    separator("6. Lazy API Pagination")

    pages = fetch_pages(5)

    print(next(pages))
    print(next(pages))


# ---------------------------------------------------------
# Memory Efficient Processing
# ---------------------------------------------------------

def memory_efficient_example():
    separator("7. Memory Efficient Processing")

    large_data = (number for number in range(1000000))

    print("Generator created.")

    print("First value:", next(large_data))
    print("Second value:", next(large_data))


# ---------------------------------------------------------
# Real-World AI Example
# ---------------------------------------------------------

def document_chunk_generator(documents):
    for document in documents:
        words = document.split()

        chunk_size = 3

        for index in range(0, len(words), chunk_size):
            yield words[index:index + chunk_size]


def real_world_example():
    separator("8. Real-World RAG Document Chunking")

    documents = [
        "Python is widely used for AI development",
        "Generators help process large documents efficiently"
    ]

    chunks = document_chunk_generator(documents)

    for chunk in chunks:
        print("Chunk:", chunk)


def main():
    eager_evaluation_example()
    lazy_evaluation_example()
    pipeline_example()
    infinite_processing_example()
    large_file_processing_example()
    pagination_example()
    memory_efficient_example()
    real_world_example()


if __name__ == "__main__":
    main()