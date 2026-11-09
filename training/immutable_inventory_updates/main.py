'''# def add_item(inventory: tuple, name: str, quantity: int) -> tuple[tuple[str,int]]:
#     updated:tuple[tuple[str,int]] = (())
#     for item in inventory:
#         if item[0] != name:
#             updated += [name, quantity]
#         else:
#             updated += item
#         return updated'''


''' STOP TRYING TO DO SO MUCH IN ONE PIECE OF CODE!!!

Think about what add_item is asked to do:
    * If the item already exists in inventory, return inventory completely unchanged.
    * If it does not exist, add ((name, quantity),) to the end of inventory.

Notice that in both cases, the existing items in inventory never need to change! '''

def add_item(inventory, name, quantity):
    for item in inventory:
        if item[0] == name:
            return inventory  # Found it! Return original unchanged immediately.
    return inventory + ((name, quantity),)
        # NBNBNB!!!!!! To add a single item to a tuple of pairs, the new pair needs to be wrapped inside its own single-element tuple (with a trailing comma)
    
    ''' 
    # NBNBNB!! if-statements DON'T need an ELSE counterpart!
    Unlike try, which syntactically requires an except or finally block to catch errors, an if statement is completely standalone. If the condition evaluates to False and there is no else, Python simply moves on to the next line of code below the if block.

    In fact, using an if statement without an else to return early (often called a guard clause or early return) is considered standard best practice in programming because it:

    * Keeps code cleaner and less indented
    * Avoids unnecessary operations (like redundant variable assignments)
    * Makes the intent obvious: "If we find a duplicate, stop right here; otherwise, keep going."'''

def change_quantity(inventory, name, quantity):
    updated:tuple[tuple[str,int]] = (())
    for item in inventory:
        if name == item[0]:
            updated += ((name, quantity),)
        elif name != item[0]:
            updated += ((item[0], item[1]),)
    return updated
    # NBNBNB!!! This return HAS TO BE outside the loop. We want the fxn to loop through the entire list BEFORE returning anything.


def remove_item(inventory, name):
    updated:tuple[tuple[str,int]] = (())
    for item in inventory:
        if name != item[0]:
            updated += ((item[0], item[1]),)
        elif name == item[0]:
            pass
    return updated
