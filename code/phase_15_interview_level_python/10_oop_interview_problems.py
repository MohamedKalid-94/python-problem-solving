"""
Phase 15 - Interview-Level Python
10 OOP Interview Problems
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient balance")
        self.balance -= amount

    def show_balance(self):
        print("Balance:", self.balance)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


def main():
    account = BankAccount("Kalid", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.show_balance()

    try:
        account.withdraw(5000)
    except ValueError as error:
        print("Error:", error)

    employee = Employee("John", 50000)
    employee.display()


if __name__ == "__main__":
    main()