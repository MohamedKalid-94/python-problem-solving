# Phase 14 - Real World Python
# Project 10 - Contact Book

contacts={}

def add_contact():
    name=input("Name: ")
    contacts[name]={"phone":input("Phone: "),"email":input("Email: ")}
    print("Contact Added")

def view_contacts():
    for contact in contacts.items(): print(contact)

def search_contact():
    name=input("Name: ")
    print(contacts.get(name,"Not Found"))

def delete_contact():
    name=input("Name: ")
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else: print("Not Found")

def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Delete\n5.Exit")
        choice=input("Choice: ")
        if choice=="1": add_contact()
        elif choice=="2": view_contacts()
        elif choice=="3": search_contact()
        elif choice=="4": delete_contact()
        elif choice=="5": break

if __name__=="__main__": main()