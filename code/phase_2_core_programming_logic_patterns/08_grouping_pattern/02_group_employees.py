"""
Topic: Group Employees

Problem:
Group employees by department.
"""

employees = [
    ("John", "HR"),
    ("Sara", "IT"),
    ("Mike", "HR"),
    ("Emma", "Finance")
]

departments = {}

for name, department in employees:
    departments.setdefault(department, []).append(name)

print(departments)