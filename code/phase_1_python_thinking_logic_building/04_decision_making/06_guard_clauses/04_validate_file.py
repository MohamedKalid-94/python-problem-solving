"""
Topic: Guard Clauses

Problem:
Validate file before uploading.

Rules:
- File should exist
- File type should be allowed
"""


file_exists = True

file_type = "pdf"


if file_exists == False:
    print("File not found")

elif file_type != "pdf":
    print("Invalid file format")

else:
    print("File uploaded successfully")