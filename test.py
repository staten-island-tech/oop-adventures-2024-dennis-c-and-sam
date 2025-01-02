import json
import random
import os

# Define the item class
class Item:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        # Convert the item object to a dictionary for JSON serialization
        return {"item": self.name, "description": self.description, "price": self.price}

# Define a list of available items
item_dict = [
    {"name": "speed_potion", "description": "Increases speed", "price": 5},
    {"name": "ladder", "description": "Allows you to jump over one wall", "price": 10},
    {"name": "slingshot", "description": "Stuns monster for a short amount of time", "price": 15}
]

# Initialize a new inventory if the file doesn't exist
if not os.path.exists('shop.json'):
    new_json = {"inventory": []}
else:
    # Read the existing content from the file
    with open('shop.json', 'r') as shop_file:
        new_json = json.load(shop_file)

# Add 3 random items to the inventory
for i in range(3):
    item_data = random.choice(item_dict)
    item_to_add = Item(item_data["name"], item_data["description"], item_data["price"])

    # Add the item to the inventory
    new_json["inventory"].append(item_to_add.to_dict())

# Write the updated inventory back to the shop.json file
with open('shop.json', 'w') as shop_file:
    json.dump(new_json, shop_file, indent=4)

# Optional: Print the updated shop.json content
print(json.dumps(new_json, indent=4))
