import random

class item:
        def __init__(self, item: str, description:str , price: int,):
            self.item = item
            self.description= description
            self.price= price

item_dict = [( "speed_potion",  "Increases speed", 5 ),
                    ( "ladder","allows you jump over one wall", 10),
                   ("dash",  "makes you dash in a certain direction", 5)]
        
shop_items=[]

for i in range(3):
            item_random = random.choice(item_dict)
            shop_items.append(item_random)

while shopping != "done":
        shopping=input("what would you like to buy? type done if done shopping.").capitalize()

class mc():
    def __init__(self,inventory,money,speed):
        self.inventory = inventory
        inventory=[]
        self.money = money
        self.speed = speed
    def buy(self, item):
           self.inventory.append(item)

