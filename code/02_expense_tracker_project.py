# Phase 14 - Real World Python
# Project 02 - Expense Tracker

expenses=[]


def add_expense():

    category=input("Enter category: ")

    amount=float(input("Enter amount: "))

    expense={
        "category":category,
        "amount":amount
    }

    expenses.append(expense)

    print("Expense Added")


def view_expenses():

    if not expenses:
        print("No expenses found")
        return

    print("\nExpense List")

    for index,expense in enumerate(expenses,1):

        print(
            index,
            expense["category"],
            expense["amount"]
        )


def total_expense():

    total=0

    for expense in expenses:

        total+=expense["amount"]

    print(
        "Total Expense:",
        total
    )


def category_summary():

    summary={}

    for expense in expenses:

        category=expense["category"]

        amount=expense["amount"]

        summary[category]=summary.get(category,0)+amount


    print("\nCategory Summary")

    for category,amount in summary.items():

        print(
            category,
            amount
        )


def main():

    while True:

        print(
            """
Expense Tracker

1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Exit
"""
        )

        choice=input("Choose option: ")


        if choice=="1":

            add_expense()


        elif choice=="2":

            view_expenses()


        elif choice=="3":

            total_expense()


        elif choice=="4":

            category_summary()


        elif choice=="5":

            print("Expense Tracker Closed")
            break


        else:

            print("Invalid Choice")


if __name__=="__main__":

    main()