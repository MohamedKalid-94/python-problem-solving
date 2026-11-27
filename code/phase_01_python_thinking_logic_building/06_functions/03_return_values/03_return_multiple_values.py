"""
Topic: Return Multiple Values

Problem:
Return name and age.
"""


def student():

    name = "Kalid"
    age = 25

    return name, age


student_name, student_age = student()

print(student_name)
print(student_age)