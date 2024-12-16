import json
import os
test= open("items.json", encoding="utf8")
items= json.load(test)
import random

with open ("shop.json", "r", encoding='utf-8-sig') as f:
    shop_items = json.load(f)

class shop:
    def __init__(self, item: str, description:str , price: int):
        self.item = item
        self.description= description
        self.price= price

ranitem = random.choice(items)
print (ranitem)

shop_items.append(ranitem)