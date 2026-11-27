# Phase 14 - Real World Python
# Project 09 - Employee Management System

employees=[]

def add_employee():
    employees.append({"id":input("ID: "),"name":input("Name: "),"department":input("Department: "),"salary":float(input("Salary: "))})
    print("Employee Added")

def view_employee():
    for employee in employees: print(employee)

def search_employee():
    eid=input("Employee ID: ")
    for employee in employees:
        if employee["id"]==eid:
            print(employee)
            return
    print("Not Found")

def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Exit")
        choice=input("Choice: ")
        if choice=="1": add_employee()
        elif choice=="2": view_employee()
        elif choice=="3": search_employee()
        elif choice=="4": break

if __name__=="__main__": main()