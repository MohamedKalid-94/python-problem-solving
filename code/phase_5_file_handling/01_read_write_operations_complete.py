"""
=========================================================
Topic : File Read and Write Operations

Author: Mohamed Kalid

Covered:
1. Create and write files
2. Read complete file
3. Read line by line
4. Count words
5. Search text
6. Replace text
7. Copy file content
8. Log analysis example
9. AI document processing example

=========================================================
"""

from pathlib import Path
from collections import Counter

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def create_and_write_file():
    separator("1. Create and Write File")
    file_name = "sample.txt"
    with open(file_name, "w") as file:
        file.write("Python is powerful\n")
        file.write("Python is used in AI\n")
        file.write("Python supports Generative AI\n")

    print("File created successfully")


def read_complete_file():
    separator("2. Read Complete File")
    file_name = "sample.txt"
    with open(file_name, "r") as file:
        content = file.read()
    print(content)


def read_line_by_line():
    separator("3. Read File Line by Line")
    file_name = "sample.txt"
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())


def count_words():
    separator("4. Word Frequency Counter")
    file_name = "sample.txt"
    with open(file_name, "r") as file:
        content = file.read()
    words = content.lower().split()
    frequency = Counter(words)
    print(frequency)


def search_text():
    separator("5. Search Text in File")
    file_name = "sample.txt"
    search_word = "AI"
    with open(file_name, "r") as file:
        content = file.read()
    if search_word.lower() in content.lower():
        print(f"{search_word} found")
    else:
        print(f"{search_word} not found")


def replace_text():
    separator("6. Replace Text")
    file_name = "sample.txt"
    with open(file_name, "r") as file:
        content = file.read()
    updated_content = content.replace(
        "Python",
        "Python Programming"
    )
    with open("updated_sample.txt", "w") as file:
        file.write(updated_content)
    print("Text replaced successfully")


def copy_file_content():
    separator("7. Copy File Content")
    source = "sample.txt"
    destination = "backup.txt"
    with open(source, "r") as source_file:
        content = source_file.read()
    with open(destination, "w") as destination_file:
        destination_file.write(content)
    print("File copied successfully")


def log_file_analyzer():
    separator("8. Log File Analyzer Problem")
    logs = """
INFO Server Started
ERROR Database Failed
WARNING Memory Usage High
ERROR API Timeout
INFO Request Completed
"""
    with open("application.log", "w") as file:
        file.write(logs)
    error_count = 0
    info_count = 0
    warning_count = 0

    with open("application.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "INFO" in line:
                info_count += 1
            elif "WARNING" in line:
                warning_count += 1
    print(
        {
            "ERROR": error_count,
            "INFO": info_count,
            "WARNING": warning_count
        }
    )


def document_processing_example():
    separator("9. AI Document Processing Example")
    documents = """
    Artificial Intelligence is transforming industries.
    Retrieval Augmented Generation improves LLM accuracy.
    Python is widely used for AI development.
    """
    with open("document.txt", "w") as file:
        file.write(documents)
    with open("document.txt", "r") as file:
        content = file.read()
    sentences = [
        sentence.strip()
        for sentence in content.split(".")
        if sentence.strip()
    ]

    print("Document chunks:")
    for chunk in sentences:
        print(chunk)



def file_information():
    separator("10. File Information")
    file = Path("sample.txt")
    if file.exists():
        print("File Name:", file.name)
        print("File Size:", file.stat().st_size, "bytes")
        print("Extension:", file.suffix)

    else:
        print("File does not exist")



def main():
    create_and_write_file()
    read_complete_file()
    read_line_by_line()
    count_words()
    search_text()
    replace_text()
    copy_file_content()
    log_file_analyzer()
    document_processing_example()
    file_information()


if __name__ == "__main__":
    main()