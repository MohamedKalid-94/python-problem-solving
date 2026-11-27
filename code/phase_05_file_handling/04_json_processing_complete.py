"""
=========================================================
Topic : JSON File Processing in Python

Author: Mohamed Kalid

Covered:

1. Create JSON files
2. Read JSON files
3. Write JSON files
4. Update JSON data
5. Nested JSON processing
6. API response handling
7. Configuration management
8. AI/RAG metadata storage

=========================================================
"""
import json
from pathlib import Path

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def create_json_file():
    separator("1. Create JSON File")
    user_data = {
        "id": 101,
        "name": "Kalid",
        "role": "AI Engineer",
        "skills": [
            "Python",
            "RAG",
            "LangChain"
        ]
    }

    with open("user.json", "w") as file:
        json.dump(
            user_data,
            file,
            indent=4
        )

    print("JSON file created")

def read_json_file():
    separator("2. Read JSON File")
    with open("user.json", "r") as file:
        data = json.load(file)
    print(data)

def update_json_data():
    separator("3. Update JSON Data")
    with open("user.json", "r") as file:
        data = json.load(file)
    data["skills"].append(
        "LangGraph"
    )
    data["experience"] = "8 years"
    with open("updated_user.json", "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )
    print("JSON updated")

def json_to_string_conversion():
    separator("4. JSON Serialization")
    data = {
        "model": "LLM",
        "temperature": 0.7
    }
    json_string = json.dumps(data)
    print(json_string)

def string_to_json_conversion():
    separator("5. JSON Deserialization")
    json_string = """
    {
        "name": "GPT",
        "type": "LLM"
    }
    """
    data = json.loads(json_string)
    print(data)

def nested_json_processing():
    separator("6. Nested JSON Processing")
    company = {
        "name": "AI Company",
        "employees": [
            {
                "name": "Alice",
                "role": "Developer"
            },
            {
                "name": "Bob",
                "role": "Tester"
            }
        ]
    }

    developers = [
        employee["name"]
        for employee in company["employees"]
        if employee["role"] == "Developer"
    ]
    print(developers)

def api_response_processing():
    separator("7. API Response Processing")
    api_response = {
        "status": "success",
        "users": [
            {
                "id": 1,
                "active": True
            },
            {
                "id": 2,
                "active": False
            },
            {
                "id": 3,
                "active": True
            }
        ]
    }


    active_users = [
        user["id"]
        for user in api_response["users"]
        if user["active"]
    ]

    print(
        "Active Users:",
        active_users
    )

def configuration_manager():
    separator("8. Configuration Management")
    config = {
        "model": "gemini",
        "temperature": 0.2,
        "max_tokens": 1000
    }

    with open("config.json", "w") as file:
        json.dump(
            config,
            file,
            indent=4
        )

    with open("config.json", "r") as file:
        loaded_config = json.load(file)
    print(loaded_config)

def rag_metadata_storage():
    separator("9. RAG Metadata Storage")
    documents = [
        {
            "document_id": "doc1",
            "topic": "Python",
            "chunks": 5
        },
        {
            "document_id": "doc2",
            "topic": "RAG",
            "chunks": 8
        }
    ]

    metadata = {
        document["document_id"]: {
            "topic": document["topic"],
            "chunks": document["chunks"]
        }
        for document in documents
    }


    with open(
        "metadata.json",
        "w"
    ) as file:
        json.dump(
            metadata,
            file,
            indent=4
        )
    print(metadata)

def json_data_validation():
    separator("10. JSON Validation")
    users = [
        {
            "name": "Alice",
            "email": "alice@gmail.com"
        },
        {
            "name": "",
            "email": "invalid"
        }
    ]

    valid_users = [
        user
        for user in users
        if user["name"]
        and "@gmail.com" in user["email"]
    ]
    print(valid_users)

def pathlib_json_operations():
    separator("11. JSON File Information")
    file = Path("user.json")
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
    create_json_file()
    read_json_file()
    update_json_data()
    json_to_string_conversion()
    string_to_json_conversion()
    nested_json_processing()
    api_response_processing()
    configuration_manager()
    rag_metadata_storage()
    json_data_validation()
    pathlib_json_operations()

if __name__ == "__main__":
    main()