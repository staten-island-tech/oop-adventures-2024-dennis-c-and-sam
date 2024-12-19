import json
import random
import os

test= open("items.json", encoding="utf8")
items= json.load(test)

# New JSON to add an item to
new_json = {
    "inventory": []
}

for i in range(3):

    item_to_add = random.choice(items)  

    try:
        with open('shop.json', 'r') as shop_file:
            shop_data = json.load(shop_file)
    except FileNotFoundError:
        shop_data = {"inventory": []}  # Start with an empty inventory if the file doesn't exist

    # Step 4: Add the extracted item to the 'inventory' in 'shop.json'
    shop_data["inventory"].append(item_to_add)

    # Step 5: Write the updated shop_data back to 'shop.json'
    with open('shop.json', 'w') as shop_file:
        json.dump(shop_data, shop_file, indent=4)

    # Optional: Print the updated shop.json content
    print(json.dumps(shop_data, indent=4))

""" new_file = "update.json"
    with open(new_file, "w")as f:
        json_string = json.dumps(shop_data)
        f.write(json_string)
    os.remove("shop.json")
    os.rename(new_file) """
