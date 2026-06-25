import json

student_list = [{"Name" : "Vinita", "Roll_No" : 23, "Marks" : 88}, {"Name" : "Vishal", "Roll_No" : 24, "Marks" : 79}, {"Name" : "Riya", "Roll_No" : 25, "Marks" : 82}]

def stud_add():
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    new_student = {"Name": name, "Roll_No": roll, "Marks": marks}
    student_list.append(new_student)

def stud_view():
    for item in student_list:
        print(item)

def stud_search():
    userask = int(input("Your Roll_No is : "))
    found = False
    for el in student_list:
        ansroll_no = el["Roll_No"]
        if userask == ansroll_no:
            print("Found")
            found = True
            break
        
    if found == False:
            print("Not Found")

def stud_update():
    userask = int(input("Your Roll_no to update is : "))
    new_marks = int(input("enter new marks : "))
    found = False
    for el in student_list:
        if el["Roll_No"] == userask:
             el["Marks"]  = new_marks
             found = True
             break
    
    if found == False:
            print("Not Found")

def stud_delete():
    userask = int(input("Your Roll_no to delete is : "))
    found = False
    for el in student_list:
        if el["Roll_No"] == userask:
             student_list.remove(el)
             found = True
             break
    
    if found == False:
            print("Not Found")
     
        
    
    
with open("students_rec.txt", "r") as f:
    student_list = json.load(f)
while True:
    menu = ("1. Add, 2. View, 3. Search, 4. Update, 5. Delete, 6. Exit")
    print(menu)
    usergive = int(input("drop your no : "))
    if usergive == 1:
        stud_add()
    elif usergive == 2:
        stud_view()
    elif usergive == 3:
        stud_search()
    elif usergive == 4:
        stud_update()
    elif usergive == 5:
        stud_delete()
    elif usergive == 6:
        with open("students_rec.txt", "w") as f:
            json.dump(student_list, f)
        print("Exit")
        break

    


        



    











