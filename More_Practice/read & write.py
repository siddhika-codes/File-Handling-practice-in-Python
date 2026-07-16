# task1 Simple Write & Read — Ek text file mein apna naam aur 3 hobbies likho ("w" mode), 
# phir usी file ko padhke print karo ("r" mode)
with open("read.txt", "w") as f:
    f.write(" Name : Siddhika Vinita Aajna\n")
    f.write(" Hobbies : Travelling\n")
    f.write(" Hobbies : Eating\n")
    f.write(" Hobbies : Reading Books\n")

with open("read.txt", "r") as f:
    mydata = f.read()
    print(mydata)



