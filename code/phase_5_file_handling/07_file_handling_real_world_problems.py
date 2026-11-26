"""
=========================================================
Topic : File Handling Real World Problems

Author: Mohamed Kalid

Covered:

1. Log Analyzer
2. CSV to JSON Data Pipeline
3. Document Processing Pipeline
4. Configuration Manager
5. Duplicate File Detector
6. AI/RAG Document Loader Simulation

Concepts Used:

- File Read/Write
- CSV
- JSON
- Pathlib
- Dictionary
- List Comprehension
- Exception Handling
- Data Processing

=========================================================
"""

import csv
import json
from pathlib import Path
from collections import Counter
import hashlib

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# =====================================================
# Problem 1: Log Analyzer
# =====================================================
def log_analyzer():
    separator("1. Application Log Analyzer")

    log_content = """
INFO Server Started
ERROR Database Connection Failed
WARNING Memory Usage High
ERROR API Timeout
INFO User Login Successful
ERROR File Processing Failed
"""
    log_file = Path(
        "application.log"
    )
    log_file.write_text(
        log_content
    )
    log_count = Counter()
    with open(
        log_file,
        "r"
    ) as file:
        for line in file:
            level = line.split()[0]
            log_count[level] += 1

    print(
        dict(log_count)
    )

# =====================================================
# Problem 2: CSV to JSON Pipeline
# =====================================================

def csv_to_json_pipeline():
    separator("2. CSV to JSON Data Pipeline")
    csv_file = Path(
        "employees.csv"
    )
    json_file = Path(
        "employees.json"
    )
    employees = [

        ["id", "name", "role"],

        [1, "Alice", "Developer"],

        [2, "Bob", "Tester"],

        [3, "Chris", "AI Engineer"]
    ]
    with open(
        csv_file,
        "w",
        newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerows(employees)

    data = []
    with open(
        csv_file,
        "r"
    ) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(
        json_file,
        "w"
    ) as file:
        json.dump(
            data,
            file,
            indent=4
        )
    print(
        "CSV converted to JSON"
    )

# =====================================================
# Problem 3: Document Processing Pipeline
# =====================================================

def document_processing_pipeline():
    separator("3. Document Processing Pipeline")
    folder = Path(
        "documents"
    )
    folder.mkdir(
        exist_ok=True
    )
    documents = {
        "python.txt":
        "Python is used for AI development",
        "rag.txt":
        "RAG improves LLM response accuracy",
        "llm.txt":
        "Large Language Models understand text"
    }

    for name, content in documents.items():
        file = folder / name
        file.write_text(
            content
        )
    processed_documents = []
    for file in folder.glob("*.txt"):
        content = file.read_text()
        chunks = [
            sentence.strip()
            for sentence in content.split(".")
            if sentence.strip()
        ]
        processed_documents.append(
            {
                "file": file.name,
                "chunks": chunks
            }
        )
    print(
        processed_documents
    )



# =====================================================
# Problem 4: Configuration Manager
# =====================================================

def configuration_manager():
    separator("4. Configuration Manager")
    config_file = Path(
        "config.json"
    )
    config = {
        "model": "gemini",
        "temperature": 0.2,
        "max_tokens": 1000
    }

    with open(
        config_file,
        "w"
    ) as file:
        json.dump(
            config,
            file,
            indent=4
        )

    with open(
        config_file,
        "r"
    ) as file:
        loaded_config = json.load(file)

    loaded_config["temperature"] = 0.5

    with open(
        config_file,
        "w"
    ) as file:
        json.dump(
            loaded_config,
            file,
            indent=4
        )
    print(
        loaded_config
    )

# =====================================================
# Problem 5: Duplicate File Detector
# =====================================================
def duplicate_file_detector():
    separator("5. Duplicate File Detector")
    folder = Path(
        "duplicate_check"
    )
    folder.mkdir(
        exist_ok=True
    )
    files = {
        "file1.txt":
        "Python AI",
        "file2.txt":
        "Python AI",
        "file3.txt":
        "Machine Learning"
    }

    for name, content in files.items():
        (folder / name).write_text(
            content
        )

    file_hashes = {}
    for file in folder.glob("*"):
        content = file.read_bytes()
        file_hash = hashlib.md5(
            content
        ).hexdigest()

        if file_hash in file_hashes:
            print(
                "Duplicate:",
                file.name,
                file_hashes[file_hash]
            )
        else:
            file_hashes[file_hash] = file.name

# =====================================================
# Problem 6: AI/RAG Document Loader
# =====================================================
def rag_document_loader():
    separator("6. RAG Document Loader Simulation")
    folder = Path(
        "knowledge_base"
    )
    folder.mkdir(
        exist_ok=True
    )
    files = {
        "ai.txt":
        "Artificial Intelligence and Machine Learning",
        "rag.txt":
        "Retrieval Augmented Generation uses vector databases"
    }

    for name, content in files.items():
        (folder / name).write_text(
            content
        )

    documents = []
    for file in folder.glob("*.txt"):
        text = file.read_text()
        document = {
            "metadata": {
                "filename": file.name,
                "size": file.stat().st_size
            },
            "content": text
        }
        documents.append(
            document
        )

    with open(
        "rag_metadata.json",
        "w"
    ) as file:
        json.dump(
            documents,
            file,
            indent=4
        )
    print(
        "Documents prepared for embedding pipeline"
    )

def main():
    log_analyzer()
    csv_to_json_pipeline()
    document_processing_pipeline()
    configuration_manager()
    duplicate_file_detector()
    rag_document_loader()

if __name__ == "__main__":
    main()