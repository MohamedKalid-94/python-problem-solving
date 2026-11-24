"""
Problem:
Calculate Net Salary.

Pattern:
Multi-Step Calculation
"""


def salary_calculator(basic_salary, hra, allowance, tax):

    gross_salary = basic_salary + hra + allowance

    net_salary = gross_salary - tax

    return {
        "gross_salary": gross_salary,
        "net_salary": net_salary
    }


if __name__ == "__main__":
    print(salary_calculator(50000, 10000, 5000, 8000))