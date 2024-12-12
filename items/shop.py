import json
test= open("./items.json", encoding="utf8")
items= json.load(test)
import random

class shop:
    def __init__(self, item: str, description:str , price: int):
        self.item = item
        self.description= description
        self.price= price

ranitem = random.choice(items)
print (ranitem)