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

class player:
    def __init__(self,inventory,money,speed):
        self.inventory = inventory
        inventory=[]
        self.money = money
        money= 100
        self.speed = speed
    def buy(self, item):
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            print(f"You have bought {item.name}. You now have {self.money} money left.")
        else:
            print("You don't have enough money for this item!")

shopping=0
while shopping != "done".capitalize():
        shopping=input("what would you like to buy? type done if done shopping.").capitalize()

        if shopping == "done":
            break

for item in player.inventory:
    print(f"{item.item}: {item.description}")