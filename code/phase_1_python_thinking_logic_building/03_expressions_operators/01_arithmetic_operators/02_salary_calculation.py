"""
Topic: Arithmetic Operators

Concept:
Calculate employee salary using arithmetic operators.
"""

basic_salary = 50000

hra = 10000

bonus = 5000

tax = 8000


gross_salary = basic_salary + hra + bonus

net_salary = gross_salary - tax


print("Employee Salary")
print("----------------")

print("Basic Salary :", basic_salary)
print("HRA :", hra)
print("Bonus :", bonus)
print("Gross Salary :", gross_salary)

print()

print("Tax :", tax)
print("Net Salary :", net_salary)