# task2 Append Practice — Ek "diary.txt" file banao, usme roz ek naya entry append karo ("a" mode) 
# bina purane entries delete kiye — 
# 3 alag baar chalake dikhao ki purana data safe raha
with open("diary.txt","w") as d:
    d.write("I feel so confused today.\n")
    d.write("I am feeling like giving up on coding.\n")

with open("diary.txt", "a") as d:
    d.write("I am feeling so nervous\n")

with open("diary.txt", "a") as d:
    d.write("today is good day\n")

with open("diary.txt", "a") as d:
    d.write("I am on right track\n")

with open("diary.txt", "r") as d:
    record = d.read()
    print(record)