Contact_data = [("Name", "Vinita", "PhoneNo", "8435084129", "Email", "vinitabishnoi76@gmail.com", "vinitab26@gmail.com"), ("Name", "Siddhika", "PhoneNO" , "8839411629", "Email", "siddhikabishnoi76@gmail.com", "siddhi17@gmail.com"),("Name" , "Vishal", "PhoneNO", "7689456579", "Email", "vishal65@gmail.com", "vishuu7@gamil.com")]

def add_contact():
    name = input("enter name : ")
    phone = int(input("enter your no. here : "))
    email = input("enter email : ")
    new_addition = ("Name" , name, "PhoneNo", phone, "Email", email)
    Contact_data.append(new_addition)

def contact_view():
    for item in Contact_data:
        print(item)

def contact_search():
    nameforSearch = input("enter your name here for search : ")
    found = False
    for el in Contact_data:
        if el[1] == nameforSearch:
            print("Contact is found in contactlist")
            found = True
            break

    if found == False:
        print("Your name is not in contactlist")

def delete_contact():
    delcont = input("enter name : ")
    found = False
    for el in Contact_data:
        if el[1] == delcont:
            Contact_data.remove(el)
            found = True
            break

    if found == False:
        print("Not found")

def uniqueNo():
    phone_numbers = ["9876543210", "9123456789", "8765432109", "9876512340"]
    unique = set()
    
    for number in phone_numbers:
        area = number[0:3]
        unique.add(area)
     
    print(len(unique))

def count_word():
    userinput = input("Any sentence of your choice : ")
    print(userinput.count(input("enter word : ")))

def sentence():
    userinput = input("Any sentence of your choice : ")
    words = userinput.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    print(longest)

def sentence_case():
    userinput = input("Any sentence of your choice : ")
    print(userinput.strip(), userinput.lower())
    
while True:
    Menu = ("1. Add, 2. View, 3. Search, 4. Delete, 5. Unique, 6. count, 7. longest sentence, 8. sentence case")
    print(Menu)
    userChoice = int(input("your choice : "))
    if userChoice == 1:
        add_contact()
    elif userChoice == 2:
        contact_view()
    elif userChoice == 3:
        contact_search()
    elif userChoice == 4:
        delete_contact()
    elif userChoice == 5:
        uniqueNo()
    elif userChoice == 6:
        count_word()
    elif userChoice == 7:
        sentence()
    elif userChoice == 8:
        sentence_case()
    else:
        print("EXIT")
        break

