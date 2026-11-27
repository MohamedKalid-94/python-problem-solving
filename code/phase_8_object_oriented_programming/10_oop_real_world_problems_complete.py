"""
=========================================================
Topic : Real-World OOP Problems

Project : Employee Management System

Concepts Covered:

1. Classes and Objects
2. Constructors
3. Inheritance
4. Polymorphism
5. Encapsulation
6. Abstraction
7. Magic Methods
8. Dataclasses

=========================================================
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Dataclass
# ---------------------------------------------------------

@dataclass
class Address:
    city: str
    state: str
    country: str

# ---------------------------------------------------------
# Abstract Class
# ---------------------------------------------------------

class Employee(ABC):
    company = "AI Solutions"

    def __init__(self, emp_id, name, salary, address):
        self.emp_id = emp_id
        self.name = name
        self._salary = salary
        self.address = address

    @abstractmethod
    def calculate_bonus(self):
        pass

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Company:", Employee.company)
        print("Salary:", self._salary)
        print("Address:", f"{self.address.city}, {self.address.state}, {self.address.country}")

    def __str__(self):
        return f"{self.emp_id} - {self.name}"

    def __eq__(self, other):
        return self.emp_id == other.emp_id

# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------

class Developer(Employee):
    def __init__(self, emp_id, name, salary, address, language):
        super().__init__(emp_id, name, salary, address)
        self.language = language

    def calculate_bonus(self):
        return self._salary * 0.20

    def display(self):
        super().display()
        print("Role: Developer")
        print("Language:", self.language)
        print("Bonus:", self.calculate_bonus())


# ---------------------------------------------------------
# Tester
# ---------------------------------------------------------

class Tester(Employee):
    def __init__(self, emp_id, name, salary, address, tool):
        super().__init__(emp_id, name, salary, address)
        self.tool = tool

    def calculate_bonus(self):
        return self._salary * 0.15

    def display(self):
        super().display()
        print("Role: Tester")
        print("Testing Tool:", self.tool)
        print("Bonus:", self.calculate_bonus())


# ---------------------------------------------------------
# Manager
# ---------------------------------------------------------

class Manager(Employee):
    def __init__(self, emp_id, name, salary, address, team_size):
        super().__init__(emp_id, name, salary, address)
        self.team_size = team_size

    def calculate_bonus(self):
        return self._salary * 0.25

    def display(self):
        super().display()
        print("Role: Manager")
        print("Team Size:", self.team_size)
        print("Bonus:", self.calculate_bonus())


# ---------------------------------------------------------
# Employee Management System
# ---------------------------------------------------------

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(employee.name, "added successfully.")

    def display_all(self):
        separator("Employee Details")

        for employee in self.employees:
            employee.display()
            print("-" * 60)

    def total_employees(self):
        print("Total Employees:", len(self.employees))

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("Employee Found")
                employee.display()
                return
        print("Employee not found.")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():
    separator("Employee Management System")

    address1 = Address("Bengaluru", "Karnataka", "India")
    address2 = Address("Chennai", "Tamil Nadu", "India")
    address3 = Address("Hyderabad", "Telangana", "India")

    developer = Developer(101, "Kalid", 90000, address1, "Python")
    tester = Tester(102, "John", 70000, address2, "Selenium")
    manager = Manager(103, "Alice", 120000, address3, 12)

    system = EmployeeManagementSystem()
    system.add_employee(developer)
    system.add_employee(tester)
    system.add_employee(manager)
    system.display_all()

    separator("Polymorphism")
    employees = [developer, tester, manager]

    for employee in employees:
        print(employee.name, "Bonus:", employee.calculate_bonus())

    separator("Magic Methods")
    print(developer)
    print("Developer == Tester :", developer == tester)
    another_developer = Developer(101, "Kalid", 90000, address1, "Python")
    print("Developer == Another Developer :", developer == another_developer)
    separator("Employee Search")
    system.search_employee(102)
    separator("Summary")
    system.total_employees()

if __name__ == "__main__":
    main()