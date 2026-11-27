"""
=========================================================
Topic : Encapsulation in Python

Covered:

1. Public Members
2. Protected Members
3. Private Members
4. Getter Methods
5. Setter Methods
6. Real-World Example

=========================================================
"""
def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Public Members
# ---------------------------------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

def public_member_example():
    separator("1. Public Members")
    student = Student("Kalid", 90)
    student.display()
    student.marks = 95
    print("Updated Marks:", student.marks)

# ---------------------------------------------------------
# Protected Members
# ---------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    def display(self):
        print("Employee:", self.name)
        print("Salary:", self._salary)

def protected_member_example():
    separator("2. Protected Members")
    employee = Employee("Alice", 65000)
    employee.display()
    employee._salary = 70000
    print("Updated Salary:", employee._salary)

# ---------------------------------------------------------
# Private Members
# ---------------------------------------------------------
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)

def private_member_example():
    separator("3. Private Members")
    account = BankAccount("Kalid", 10000)
    account.display()
    print("Private members cannot be accessed directly.")

# ---------------------------------------------------------
# Getter and Setter Methods
# ---------------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
            print("Price updated successfully.")
        else:
            print("Invalid price.")

    def display(self):
        print("Product:", self.name)
        print("Price:", self.__price)


def getter_setter_example():
    separator("4. Getter and Setter Methods")
    product = Product("Laptop", 75000)
    product.display()
    print("Current Price:", product.get_price())
    product.set_price(80000)
    product.display()
    product.set_price(-100)


# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------
class User:
    def __init__(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_username(self, username):
        if len(username) >= 4:
            self.__username = username
            print("Username updated.")
        else:
            print("Username must contain at least 4 characters.")


def validation_example():
    separator("5. Data Validation")
    user = User("kalid")
    print("Username:", user.get_username())
    user.set_username("john")
    print("Updated Username:", user.get_username())
    user.set_username("ab")

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class ATMAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Available Balance:", self.__balance)


def real_world_example():
    separator("6. Real-World ATM System")
    account = ATMAccount("Kalid", 20000)
    account.check_balance()
    account.deposit(5000)
    account.withdraw(8000)
    account.check_balance()

def main():
    public_member_example()
    protected_member_example()
    private_member_example()
    getter_setter_example()
    validation_example()
    real_world_example()

if __name__ == "__main__":
    main()