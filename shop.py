import json
import os
test= open("items.json", encoding="utf8")
items= json.load(test)
import random


class item:
    def __init__(self, item: str, description:str , price: int):
        self.item = item
        self.description= description
        self.price= price

ranitem = random.choice(items)
print (ranitem)

with open("./json/shop.json", "r") as f:
    shop_items = json.load(f)
    shop_items.append(ranitem)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(shop_items)
    f.write(json_string)
os.remove("shop.json")
os.rename(new_file, "shop.json")