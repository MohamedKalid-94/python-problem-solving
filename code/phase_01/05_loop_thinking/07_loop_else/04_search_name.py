"""
Topic: Loop else

Problem:
Search for a student name.
"""

students = ["Arun", "Priya", "Rahul", "Kiran"]

search_name = "Kiran"

for student in students:

    if student == search_name:
        print("Student Found")
        break

else:
    print("Student Not Found")