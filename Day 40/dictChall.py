# Task 1: Create a dictionary representing a collection of items in a store. Each key is the item name, and the value is the price of the item. (All prices in Rupees)

store_items = {"bread": 140, "milk": 200, "yogurt": 240, "cake": 100} 

print(store_items) # {'bread': 140, 'milk': 200, 'yogurt': 240, 'cake': 100}

# Task 2: Add a new item to the dictionary (adding egg)

store_items.update({"egg": 250}) 

print(store_items) # {'bread': 140, 'milk': 200, 'yogurt': 240, 'cake': 100, 'egg': 250}

# Task 3: Update the price of an existing item. (cake to 80 Rupees)

store_items.update({"cake": 80})

print(store_items) # {'bread': 140, 'milk': 200, 'yogurt': 240, 'cake': 80, 'egg': 250}

# Task 4: Remove an item from the dictionary. (Removing cake)

store_items.pop("cake")
print(store_items) # {'bread': 140, 'milk': 200, 'yogurt': 240, 'egg': 250}

# Task 5: Calculate the total value of all items in the dictionary.

total_value = 0

for value in store_items.values():
    total_value += value

print(f"Total value of all the items is Rs {total_value}")  # Total value of all the items is Rs 830



# Task 6: Print out each item and its price in a formatted way

for key,value in store_items.items():
    print(f"Get {key} in only Rs {value}")

