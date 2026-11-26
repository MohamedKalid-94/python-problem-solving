"""
Topic: Highest Salary

Problem:
Find the highest salary from a list.
"""

salaries = [45000, 62000, 58000, 73000, 51000]

highest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary

print("Highest Salary:", highest)