import json

Subjectdata = [{"subject" : "english", "completedportion" : 75, "weightageofsub" : 80},{"subject" : "science", "completedportion" : 60, "weightageofsub" : 70},{"subject" : "computer", "completedportion" : 35, "weightageofsub" : 50}]

def add_subject():
    subject = input("enter your subject here : ")
    completedportion = int(input("portion completed : "))
    weightageportion = int(input("weightage of subject to be included is : "))
    subjectadd = {"subject" : subject, "completedportion" : completedportion, "weightageofsub" : weightageportion}
    Subjectdata.append(subjectadd)

def view_subject():
    for sub in Subjectdata:
        print(sub)

def search_subject():
    subsearch = input("your subject for search is : ")
    found = False
    for el in Subjectdata:
        search = el["subject"]
        if subsearch == search:
            print("Subject is found")
            found = True
            break

    if found == False:
        print("Subject is not in the List")


def update_subject():
    subjectupdate = input("subject for update is : ")
    updated = int(input("updated portion is : "))
    found = False
    for item in Subjectdata:
        if item["subject"] == subjectupdate:
             item["completedportion"] = updated
             found = True
             break

    if found == False:
        print("Subject is not updated")


def subject_delete():
    subdelete = input("subject to delete is : ")
    for item in Subjectdata:
        delete = item["subject"]
        if subdelete == delete:
            Subjectdata.remove(item)
            break

with open("subject_data.txt", "r") as f:
    Subjectdata = json.load(f)      

while True:
    Menu = ("1. Add, 2. View, 3. Search, 4. Update, 5. Delete, 6. Exit")
    print(Menu)
    userResponse = int(input("Share your preference : "))
    if userResponse == 1:
        add_subject()
    elif userResponse == 2:
        view_subject()
    elif userResponse == 3:
        search_subject()
    elif userResponse == 4:
        update_subject()
    elif userResponse == 5:
        subject_delete()
    elif userResponse == 6:
        with open("subject_data.txt","w") as f:
            json.dump(Subjectdata, f)
        print("EXIT")
        break
            





     



