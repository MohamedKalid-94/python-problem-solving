# Phase 14 - Real World Python
# Project 08 - Password Manager

passwords={}

def add_password():
    site=input("Website: ")
    passwords[site]={"username":input("Username: "),"password":input("Password: ")}
    print("Password Saved")

def view_passwords():
    for item in passwords.items(): print(item)

def search_password():
    site=input("Website: ")
    print(passwords.get(site,"Not Found"))

def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Exit")
        choice=input("Choice: ")
        if choice=="1": add_password()
        elif choice=="2": view_passwords()
        elif choice=="3": search_password()
        elif choice=="4": break

if __name__=="__main__": main()