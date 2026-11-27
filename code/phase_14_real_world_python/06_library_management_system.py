# Phase 14 - Real World Python
# Project 06 - Library Management System

books=[]

def add_book():
    books.append({"id":input("Book ID: "),"title":input("Title: "),"author":input("Author: "),"issued":False})
    print("Book Added")

def view_books():
    for book in books: print(book)

def issue_book():
    bid=input("Book ID: ")
    for book in books:
        if book["id"]==bid:
            book["issued"]=True
            print("Book Issued")
            return
    print("Book Not Found")

def return_book():
    bid=input("Book ID: ")
    for book in books:
        if book["id"]==bid:
            book["issued"]=False
            print("Book Returned")
            return
    print("Book Not Found")

def main():
    while True:
        print("\n1.Add\n2.View\n3.Issue\n4.Return\n5.Exit")
        choice=input("Choice: ")
        if choice=="1": add_book()
        elif choice=="2": view_books()
        elif choice=="3": issue_book()
        elif choice=="4": return_book()
        elif choice=="5": break

if __name__=="__main__": main()