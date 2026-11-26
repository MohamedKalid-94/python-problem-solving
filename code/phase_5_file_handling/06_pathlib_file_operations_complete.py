"""
=========================================================
Topic : Pathlib File Operations in Python

Author: Mohamed Kalid

Covered:

1. Path object creation
2. File and folder creation
3. Check file existence
4. Read and write files
5. Rename files
6. Move files
7. Delete files
8. Search files
9. Project scanner
10. AI document processing example

=========================================================
"""
from pathlib import Path
import shutil

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def create_path_object():
    separator("1. Create Path Object")
    file_path = Path(
        "example.txt"
    )
    print(
        "File Name:",
        file_path.name
    )
    print(
        "Extension:",
        file_path.suffix
    )

def create_folder():
    separator("2. Create Folder")
    folder = Path(
        "documents"
    )
    folder.mkdir(
        exist_ok=True
    )
    print(
        "Folder created"
    )



def create_and_write_file():
    separator("3. Create and Write File")
    file_path = Path(
        "documents/data.txt"
    )
    file_path.write_text(
        "Python Pathlib Example"
    )
    print(
        "File written"
    )

def read_file():
    separator("4. Read File")
    file_path = Path(
        "documents/data.txt"
    )
    content = file_path.read_text()
    print(content)

def check_file_exists():
    separator("5. Check File Exists")
    file_path = Path(
        "documents/data.txt"
    )
    if file_path.exists():
        print(
            "File exists"
        )
    else:
        print(
            "File not found"
        )

def file_information():
    separator("6. File Information")
    file_path = Path(
        "documents/data.txt"
    )
    if file_path.exists():
        print(
            "Name:",
            file_path.name
        )
        print(
            "Size:",
            file_path.stat().st_size,
            "bytes"
        )
        print(
            "Absolute Path:",
            file_path.absolute()
        )

def rename_file():
    separator("7. Rename File")
    old_file = Path(
        "documents/data.txt"
    )
    new_file = Path(
        "documents/python_data.txt"
    )
    if old_file.exists():
        old_file.rename(
            new_file
        )
    print(
        "File renamed"
    )

def create_backup():
    separator("8. Copy File")
    source = Path(
        "documents/python_data.txt"
    )
    destination = Path(
        "backup_data.txt"
    )
    if source.exists():
        shutil.copy(
            source,
            destination
        )
    print(
        "Backup created"
    )

def move_file():
    separator("9. Move File")
    source = Path(
        "backup_data.txt"
    )
    destination_folder = Path(
        "backup"
    )
    destination_folder.mkdir(
        exist_ok=True
    )
    if source.exists():
        shutil.move(
            source,
            destination_folder / source.name
        )
    print(
        "File moved"
    )

def search_files():
    separator("10. Search Files")
    folder = Path(
        "."
    )
    python_files = list(
        folder.glob("*.py")
    )
    print(
        "Python Files:"
    )
    for file in python_files:

        print(
            file
        )

def recursive_file_search():
    separator("11. Recursive File Search")
    folder = Path(
        "."
    )
    files = list(
        folder.rglob("*.py")
    )
    print(
        "Total Python Files:",
        len(files)
    )
def delete_file():
    separator("12. Delete File")
    file_path = Path(
        "temp.txt"
    )
    file_path.write_text(
        "Temporary file"
    )
    if file_path.exists():
        file_path.unlink()
    print(
        "File deleted"
    )

def project_scanner():
    separator("13. Project Scanner")
    project = Path(
        "."
    )

    python_count = 0
    json_count = 0
    csv_count = 0

    for file in project.rglob("*"):
        if file.is_file():
            if file.suffix == ".py":
                python_count += 1
            elif file.suffix == ".json":
                json_count += 1
            elif file.suffix == ".csv":
                csv_count += 1

    print(
        {
            "Python": python_count,
            "JSON": json_count,
            "CSV": csv_count
        }
    )

def ai_document_processing():
    separator("14. AI Document Folder Processing")
    documents_folder = Path(
        "ai_documents"
    )
    documents_folder.mkdir(
        exist_ok=True
    )
    files = [
        "rag_intro.txt",
        "llm_notes.txt",
        "embedding.txt"
    ]

    for file_name in files:
        file = documents_folder / file_name
        file.write_text(
            "AI document content"
        )

    documents = list(
        documents_folder.glob("*.txt")
    )

    print(
        "Documents Found:"
    )

    for document in documents:

        print(
            document.name
        )

def main():
    create_path_object()
    create_folder()
    create_and_write_file()
    read_file()
    check_file_exists()
    file_information()
    rename_file()
    create_backup()
    move_file()
    search_files()
    recursive_file_search()
    delete_file()
    project_scanner()
    ai_document_processing()

if __name__ == "__main__":
    main()