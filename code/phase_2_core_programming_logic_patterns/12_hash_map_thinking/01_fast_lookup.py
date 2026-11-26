"""
Topic: Fast Lookup

Problem:
Use a dictionary for fast key lookup.
"""

students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

student_id = 102

if student_id in students:
    print("Student:", students[student_id])
else:
    print("Student not found")