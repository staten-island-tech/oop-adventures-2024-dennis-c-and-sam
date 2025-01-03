import random

class mc():
    def __init__(self,inventory,money,speed):
        self.inventory = inventory
        self.money = money
        self.speed = speed
    def buy(self,item,inventory):
        self.inventory= inventory
        inventory={}
        self.inventory.append(item)

class item:
        def __init__(self, item: str, description:str , price: int):
            self.item = item
            self.description= description
            self.price= price

        item_dict =[{"item": "speed_potion", "description": "Increases speed", "price": 5 },
                    {"item": "ladder", "description": "allows you jump over one wall", "price": 10},
                    {"item":"slingshot", "description": "stuns monster for a short amount of time", "price": 15}]
        shop_item=[]

        for i in range(3):
            item_random = random.choice(item_dict)
            shop_item.append(item_random)
        print(shop_item)          
       
