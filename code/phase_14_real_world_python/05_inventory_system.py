# Phase 14 - Real World Python
# Project 05 - Inventory System

inventory={}

def add_product():
    pid=input("Product ID: ")
    inventory[pid]={"name":input("Name: "),"price":float(input("Price: ")),"quantity":int(input("Quantity: "))}
    print("Product Added")

def view_products():
    for product in inventory.items(): print(product)

def update_stock():
    pid=input("Product ID: ")
    if pid in inventory:
        inventory[pid]["quantity"]=int(input("New Quantity: "))
        print("Stock Updated")
    else: print("Product Not Found")

def search_product():
    pid=input("Product ID: ")
    print(inventory.get(pid,"Product Not Found"))

def main():
    while True:
        print("\n1.Add\n2.View\n3.Update Stock\n4.Search\n5.Exit")
        choice=input("Choice: ")
        if choice=="1": add_product()
        elif choice=="2": view_products()
        elif choice=="3": update_stock()
        elif choice=="4": search_product()
        elif choice=="5": break
        else: print("Invalid Choice")

if __name__=="__main__": main()