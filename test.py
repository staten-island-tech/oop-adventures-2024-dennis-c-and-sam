import random

class Item:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

# List of items
item_dict = [
    ("speed_potion", "Increases speed", 5),
    ("ladder", "Allows you to jump over one wall", 10),
    ("dash", "Makes you dash in a certain direction", 5)
]

# List to hold item instances
shop_items = []

# Randomly selecting items from the list and creating Item objects
for item_data in item_dict:
    shop_items.append(Item(item_data[0], item_data[1], item_data[2]))

class Player:
    def __init__(self, inventory=None, money=0, speed=0):
        if inventory is None:
            inventory = []  # Initialize inventory as an empty list if not provided
        self.inventory = inventory
        self.money = money
        self.speed = speed

    def buy(self, item):
        # Check if the player has enough money to buy the item
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            print(f"You have bought {item.name}. You now have {self.money} money left.")
        else:
            print("You don't have enough money for this item!")

# Create a player object
player = Player(money=20)

# Shopping loop
shopping = ""
while shopping != "done":
    print("\nWelcome to the shop!")
    print("Items available for sale:")
    for i, item in enumerate(shop_items):
        print(f"{i + 1}. {item.name} - {item.description} - Price: {item.price} money")

    shopping = input("What would you like to buy? Type 'done' to stop shopping: ").capitalize()

    if shopping == "Done":
        print("You are done shopping.")
        break

    # Handle buying an item
    try:
        item_index = int(shopping) - 1
        if 0 <= item_index < len(shop_items):
            item_to_buy = shop_items[item_index]
            player.buy(item_to_buy)
        else:
            print("Invalid item selection.")
    except ValueError:
        print("Invalid input. Please select an item by its number or type 'done'.")

print("\nYour final inventory:")
for item in player.inventory:
    print(f"{item.name}: {item.description}")
