# Phase 14 - Real World Python
# Project 03 - Student Management System

students=[]

def add_student():
    student={"id":input("ID: "),"name":input("Name: "),"age":int(input("Age: ")),"course":input("Course: "),"marks":float(input("Marks: "))}
    students.append(student)
    print("Student Added")

def view_students():
    if not students: print("No Records"); return
    for student in students: print(student)

def search_student():
    student_id=input("Enter ID: ")
    for student in students:
        if student["id"]==student_id:
            print(student)
            return
    print("Student Not Found")

def update_student():
    student_id=input("Enter ID: ")
    for student in students:
        if student["id"]==student_id:
            student["marks"]=float(input("New Marks: "))
            print("Updated")
            return
    print("Student Not Found")

def delete_student():
    student_id=input("Enter ID: ")
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            print("Deleted")
            return
    print("Student Not Found")

def main():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Exit")
        choice=input("Choice: ")

        if choice=="1": add_student()
        elif choice=="2": view_students()
        elif choice=="3": search_student()
        elif choice=="4": update_student()
        elif choice=="5": delete_student()
        elif choice=="6": break
        else: print("Invalid Choice")

if __name__=="__main__": main()