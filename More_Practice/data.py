# task3 JSON Dump — Ek dictionary banao (jaise {"name": "Siddhika", "age": 22, "city": "Raipur"}), 
# usko json.dump() se ek .
# json file mein save karo
import json

intro = {
    "name" : "siddhika",
    "age" : 22,
    "city" : "raipur"
}

with open("intro.json", "w") as f:
    json.dump(intro, f)


with open("intro.json", "r") as f:
    info = json.load(f)
    print(info)

