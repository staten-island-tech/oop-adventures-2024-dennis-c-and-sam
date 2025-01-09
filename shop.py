import random
import pygame

pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shop Interface")

def draw_shop():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 40)
    title_text = font.render("Welcome to the Shop!", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))












class Item:
        def __init__(self, name: str, description:str , price: int,):
            self.name = name
            self.description= description
            self.price= price

item_dict = [( "speed_potion",  "Increases speed", 5 ),
                    ( "ladder","allows you jump over one wall", 10),
                   ("dash",  "makes you dash in a certain direction", 5)]
        
shop_items=[]

for i in range(3):
            item_random = random.choice(item_dict)
            shop_items.append(Item(*item_random))

class player():
    def __init__(self,inventory:list,money:int,speed:int):
        self.inventory = inventory
        self.money = money
        self.speed = speed

    def buy(self, item):
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            shop_items.remove(item)
            print(f"You have bought {item.name}. You now have {self.money} money left.")
        else:
            print("You don't have enough money for this item!")
        
mc = player(inventory=[],money=100,speed=10)

shopping = ""
while shopping.lower() != "done":
    print("Items available for sale:")
    for items in shop_items:
        print(f"{items.name}: {items.description} - Price: {items.price}")

    shopping = input("What would you like to buy? Type 'done' if done shopping: ").lower()

    if shopping == "done":
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

for items in mc.inventory:
    print("Your inventory:")
    print(f"{items.name}: {items.description}")