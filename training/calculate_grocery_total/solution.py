def calculate_total(order, prices, coupon=None):
    subtotal = 0

    for item, qty in order.items():
        if not isinstance(qty, int) or qty < 0:
            raise ValueError(f"Invalid quantity for '{item}'")
        try:
            price = prices[item]
        except KeyError:
            raise KeyError(f"Unknown item: '{item}'")
        subtotal += price * qty

    if coupon is None:
        return subtotal
    if coupon == "SAVE10":
        total = subtotal - 10
        if total < 0:
            total = 0
        return total
    if coupon == "HALF":
        return subtotal // 2

    raise ValueError("Invalid coupon")
