# task5 FileNotFoundError Handling — Ek aisi file padhne ki koshish karo jo exist hi nahi karti, 
# try/except use karke graceful error message print karo (crash na ho)

try:
    with open("sidd_info.txt","r") as f:
        data = f.read()
        print(data)
except:
    print("File not found")