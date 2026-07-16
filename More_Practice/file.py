# JSON Load — Wahi file jo task 3 mein banayi, usko json.load() 
# se wapas dictionary mein padho aur print karo
import json 

data = {"name" : "vinita", "she_is_who" : "mother"}

with open("family.json","w") as f:
    json.dump(data,f)

with open("family.json","r") as f:
    fam = json.load(f)
    print(fam)