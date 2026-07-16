# task6 Combine Karna — Ek chhota "Contacts" program: dictionary mein 2-3 contacts 
# (naam: number) daalo, json.dump() se save karo,
#  phir program dobara "restart" karne ka simulate karo 
# (naya code cell/run) — json.load() se wapas load karke print karo
import json

contacts = {
    "siddhika" : 8768765465,
    "vinita" : 7689056780,
}

with open("contacts.json","w") as f:
    json.dump(contacts,f)

with open("contacts.json","r") as f:
    data = json.load(f)
    print(data)