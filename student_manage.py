import json
import os
FILE_NAME = "student_grade.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r") as file:
        student_grade = json.load(file)
else:   
    student_grade = {}
def save_data():
    with open(FILE_NAME,"w") as file:
        json.dump(student_grade,file,indent=4)    
def add_student(name,grade):
    student_grade[name] = grade
    print("add student successfuly")
    save_data()
def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        print("update student succesfully")
    else:
        print("student not found")
    save_data()

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print("delete student successfully")
    else:
        print("student not found")
    save_data()    
def display_all_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("no student found")
def search_student(name):
    if name in student_grade:
        print(f"{name}:{student_grade[name]}")   
    else:
        print("student not found")         
def main():
    print("welcome to student management system")
    while True:
        user_input = int(input("1.ad student \n 2. update_student \n 3. delete student \n 4. display all student \n 5.search student \n 6.exit" )) 
        if user_input == 1:
            name = input("enter student name: ")
            grade = input("enter student grade: ")
            add_student(name,grade)
        elif user_input == 2:
            name = input("enter student name: ")
            grade = input("enter student grade: ")
            update_student(name,grade)
        elif user_input == 3:
            name = input("enter student name: ")
            delete_student(name)
        elif user_input == 4:
            display_all_student()
        elif user_input == 5:
            name = input("enter student name: ")
            search_student(name)
        elif user_input == 6:
            break
        else:
            print("invalid input")
main()            