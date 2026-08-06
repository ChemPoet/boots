# **Calculate Grocery Total (with Errors)**

Complete the calculate_total function.

It should compute the total price of a grocery order from a price map, while handling bad input with Python exceptions.

# Inputs:

--  order: a dictionary mapping item names to quantities **(integers >= 0)**
--  prices: a dictionary mapping item names to integer prices
--  coupon (optional): one of None, "SAVE10", or "HALF"

# Behavior

1. Loop through each item, qty in order.
    If qty is not an integer or is negative, raise **ValueError("Invalid quantity for '<item>'")**.
    Look up the item price in prices. If the item is missing, raise **KeyError("Unknown item: '<item>'")**.
    Add qty * price to the subtotal.
2. Apply the coupon:
    None: no change.
    "SAVE10": subtract 10 from the subtotal, but never go below 0.
    "HALF": return half the subtotal using integer division (floor), no fractions.
    Any other value: raise **ValueError("Invalid coupon")**.
3. Return the final total as an integer.

# Notes

--  Use try/except for error handling when looking up prices and validating input.
--  Do not print inside the function; just return the result.

# Examples

    a = {"apple": 2, "banana": 3}
    prices = {"apple": 4, "banana": 2}
    print(calculate_total(a, prices))
--  # 14  (2*4 + 3*2)

    b = {"milk": 1, "bread": 1}
    prices = {"milk": 5, "bread": 3}
    print(calculate_total(b, prices, "SAVE10"))
--  # 0   (max(0, (5+3) - 10) = 0)

    c = {"rice": 3}
    prices = {"rice": 7}
    print(calculate_total(c, prices, "HALF"))
--  # 10  (3*7 = 21, 21 // 2 = 10)