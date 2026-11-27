"""
=========================================================
Topic : Methods in Python

Covered:

1. Instance Methods
2. Class Methods
3. Static Methods
4. Calling Methods
5. Object Interaction
6. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Instance Methods
# ---------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 35:
            print(self.name, "has passed.")
        else:
            print(self.name, "has failed.")

def instance_method_example():
    separator("1. Instance Methods")

    student = Student("Kalid", 82)
    student.display()
    student.is_pass()


# ---------------------------------------------------------
# Multiple Objects Calling Methods
# ---------------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

def multiple_objects_example():
    separator("2. Multiple Objects")

    employee1 = Employee("Alice", 65000)
    employee2 = Employee("Bob", 72000)

    employee1.display()
    print("-" * 30)
    employee2.display()


# ---------------------------------------------------------
# Class Methods
# ---------------------------------------------------------

class Company:
    company_name = "AI Solutions"

    @classmethod
    def display_company(cls):
        print("Company:", cls.company_name)

def class_method_example():
    separator("3. Class Method")

    Company.display_company()


# ---------------------------------------------------------
# Static Methods
# ---------------------------------------------------------

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

def static_method_example():
    separator("4. Static Method")

    print("Addition:", Calculator.add(10, 20))
    print("Multiplication:", Calculator.multiply(10, 20))

# ---------------------------------------------------------
# Object Interaction
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


def object_interaction_example():
    separator("5. Object Interaction")

    account = BankAccount("Kalid", 10000)

    account.display_balance()
    account.deposit(2500)
    account.withdraw(3000)
    account.display_balance()

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item, "removed from cart.")
        else:
            print(item, "not found.")

    def display_cart(self):
        print("Shopping Cart:", self.items)

def real_world_example():
    separator("6. Real-World Shopping Cart")

    cart = ShoppingCart()
    cart.add_item("Laptop")
    cart.add_item("Mouse")
    cart.add_item("Keyboard")
    cart.display_cart()
    cart.remove_item("Mouse")
    cart.display_cart()


def main():
    instance_method_example()
    multiple_objects_example()
    class_method_example()
    static_method_example()
    object_interaction_example()
    real_world_example()

if __name__ == "__main__":
    main()