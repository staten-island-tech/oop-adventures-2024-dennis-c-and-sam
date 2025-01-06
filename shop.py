import random

class item:
        def __init__(self, item: str, description:str , price: int):
            self.item = item
            self.description= description
            self.price= price


        item_dict = [{ "speed_potion",  "Increases speed", 5 },
                    { "ladder","allows you jump over one wall", 10},
                    {"slingshot",  "stuns monster for a short amount of time", 15}]
        
        shop_items=[]

        for i in range(3):
            item_random = random.choice(item_dict)
            shop_items.append(item_random)

            print(shop_items)

def buy(self,item,inventory):
        self.inventory= inventory
        inventory={}
        self.inventory.append(item)





