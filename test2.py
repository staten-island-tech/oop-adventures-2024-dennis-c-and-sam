import random

class Item:
    def __init__(self, item: str, description: str, price: int):
        self.item = item
        self.description = description
        self.price = price

item_dict = [
    ("speed_potion", "Increases speed", 5),
    ("ladder", "Allows you to jump over one wall", 10),
    ("dash", "Makes you dash in a certain direction", 5)
]

shop_items = []

# Convert tuples into instances of the Item class
for i in range(3):
    item_random = random.choice(item_dict)
    shop_items.append(Item(*item_random))

print(shop_items)

class Player:
    def __init__(self):
        self.inventory = []
        self.money = 100
        self.speed = 10

    def buy(self, item):
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            print(f"You have bought {item.item}. You now have {self.money} money left.")
        else:
            print("You don't have enough money for this item!")

# Create a player instance
player = Player()

shopping = ""
while shopping != "Done":
    shopping = input("What would you like to buy? Type 'done' if done shopping. ").capitalize()

    if shopping == "Done":
        break

    # Simulate the shop items being presented
    print("Items available for sale:")
    for idx, item in enumerate(shop_items, start=1):
        print(f"{idx}. {item.item}: {item.description} - Price: {item.price}")

    # Get the player's choice
    try:
        choice = int(input("Select the item number to buy: "))
        if 1 <= choice <= len(shop_items):
            selected_item = shop_items[choice - 1]
            player.buy(selected_item)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

# After shopping ends, show the player's inventory
print("\nYour inventory:")
for item in player.inventory:
    print(f"{item.item}: {item.description}")
