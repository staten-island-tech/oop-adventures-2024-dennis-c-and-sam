import json
import os
import random

# Load items from 'items.json'
with open("items.json", encoding="utf8") as test:
    items = json.load(test)

# Define Item class
class Item:
    def __init__(self, item: str, description: str, price: int):
        self.item = item
        self.description = description
        self.price = price

# Randomly pick an item from the items list
ranitem = random.choice(items)
print(ranitem)

# Read the shop items from 'shop.json' with error handling
shop_items = []
try:
    with open("./json/shop.json", "r") as f:
        shop_items = json.load(f)  # Load existing items
except json.JSONDecodeError:
    print("shop.json is empty or invalid. Initializing with an empty list.")
except FileNotFoundError:
    print("shop.json file not found. Creating a new one.")

# Append the random item
shop_items.append(ranitem)

# Save the updated list back to the 'shop.json' file
new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(shop_items, indent=4)  # Pretty print JSON
    f.write(json_string)

# Replace the old 'shop.json' with the updated one
os.remove("shop.json")
os.rename(new_file, "shop.json")

