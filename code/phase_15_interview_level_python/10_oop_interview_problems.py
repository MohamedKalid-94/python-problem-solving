# Phase 15 - Interview-Level Python
# 10 OOP Interview Problems

class BankAccount:
    def __init__(self,name,balance): self.name=name; self.balance=balance

    def deposit(self,amount): self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:self.balance-=amount

    def show_balance(self): print("Balance:",self.balance)

class Employee:
    def __init__(self,name,salary): self.name=name; self.salary=salary

    def display(self): print(self.name,self.salary)

def main():
    account=BankAccount("Kalid",1000)
    account.deposit(500)
    account.withdraw(200)
    account.show_balance()

    employee=Employee("John",50000)
    employee.display()

if __name__=="__main__": main()