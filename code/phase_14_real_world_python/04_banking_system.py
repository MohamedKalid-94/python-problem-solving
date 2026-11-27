# Phase 14 - Real World Python
# Project 04 - Banking System

accounts={}

def create_account():
    acc=input("Account No: ")
    name=input("Name: ")
    balance=float(input("Initial Balance: "))
    accounts[acc]={"name":name,"balance":balance}
    print("Account Created")

def deposit():
    acc=input("Account No: ")
    if acc in accounts:
        amount=float(input("Deposit Amount: "))
        accounts[acc]["balance"]+=amount
        print("Deposit Successful")
    else: print("Account Not Found")

def withdraw():
    acc=input("Account No: ")
    if acc in accounts:
        amount=float(input("Withdraw Amount: "))
        if accounts[acc]["balance"]>=amount:
            accounts[acc]["balance"]-=amount
            print("Withdrawal Successful")
        else: print("Insufficient Balance")
    else: print("Account Not Found")

def check_balance():
    acc=input("Account No: ")
    if acc in accounts: print(accounts[acc])
    else: print("Account Not Found")

def main():
    while True:
        print("\n1.Create\n2.Deposit\n3.Withdraw\n4.Balance\n5.Exit")
        choice=input("Choice: ")
        if choice=="1": create_account()
        elif choice=="2": deposit()
        elif choice=="3": withdraw()
        elif choice=="4": check_balance()
        elif choice=="5": break
        else: print("Invalid Choice")

if __name__=="__main__": main()