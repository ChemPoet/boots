# Immutable Inventory Updates

Complete the three inventory functions in main.py.

An inventory is a tuple containing **(name, quantity)** tuples:

    inventory = (("potion", 3), ("torch", 5))


Each function must return an inventory tuple without changing the original input.

* **add_item(inventory, name, quantity)** adds a new item to the end. If the name already exists, return the inventory unchanged.

* **change_quantity(inventory, name, quantity)** returns an inventory with that item's quantity replaced. If the item is missing, return the inventory unchanged.

* **remove_item(inventory, name)** returns an inventory without the named item. If the item is missing, return the inventory unchanged.


Keep all existing items in their original order. Do not use mutable lists or modify values in place.

    inventory = (("potion", 3), ("torch", 5))
    updated = change_quantity(inventory, "potion", 8)

    print(updated)
    # (("potion", 8), ("torch", 5))

    print(inventory)
    # (("potion", 3), ("torch", 5))



