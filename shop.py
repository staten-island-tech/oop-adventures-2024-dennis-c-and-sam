import random
import sys
import subprocess
import pygame
import os


class Item:
        def __init__(self, name: str, description:str , price: int,):
            self.name = name
            self.description= description
            self.price= price

item_dict = [( "speed_potion",  "Increases speed for 5 seconds", 15 ),
                    ( "speed_potion_2","Increases speed more,", 30),
                   ("speed_potion_long",  "increases speed for 10 seconds", 20)]
        
shop_items=[]

for i in range(3):
            item_random = random.choice(item_dict)
            shop_items.append(Item(*item_random))

class player():
    def __init__(self,inventory:list,money:int):
        self.inventory = inventory
        self.money = money

    def buy(self, item):
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            shop_items.remove(item)
            print(f"You have bought {item.name}. You now have {self.money} money left.")
        else:
            print("You don't have enough money for this item!")

    def use(self, item):
        if item in self.inventory:
            print(f"You have used {item.name}.")
            self.inventory.remove(item)

mc = player(inventory=[],money=50)

shopping = ""
while shopping.lower() != "done":
    print(f"Your money: {mc.money}")
    print("Items available for sale:")
    for items in shop_items:
        print(f"{items.name}: {items.description} - Price: {items.price}")

    shopping = input("What would you like to buy? Type 'done' if done shopping: ").lower()

    if shopping == "done":
        subprocess.Popen(["python", "game.py"])
        break

    item_found = False
    for items in shop_items:
        if items.name.lower() == shopping:
            mc.buy(items)
            item_found = True
            break

    if shop_items==[]:
        print("No more items left in the shop!")
        break

    if not item_found:
        print("Item not found!")



# useyn = ""
# while useyn != "no":
#     print("Your inventory:")
#     for items in mc.inventory:
#         print(f"{items.name}: {items.description}")
#     useyn = input("Would you like to use an item? (yes/no): ").lower()
#     if useyn == "yes":
#         use_item = input("Which item would you like to use? ")
#         item_found = False
#         for items in mc.inventory:
#             if items.name.lower() == use_item:
#                 mc.use(items)
#                 item_found = True
#                 break
#         if not item_found:
#             print("Item not found!")
#     elif useyn == "no":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid input! Please enter 'yes' or 'no'.")
            