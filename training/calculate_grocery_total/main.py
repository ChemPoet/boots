def calculate_total(order: dict[str, int], prices: dict[str, int], coupon=None):
    # order = [item: str, quant: int]
    # Confirm quant >= 0
    # price = [item: str, cost: int]
    # coupon = [None, "SAVE10", "HALF"]
    
    # Flow -> item in order -> quant >= 0
    #               |
    #       price of item -> item in price
    #               |
    #       cost = quant * price
    # var = cost    |
    #       subtotal = sum of costs
    # var = subtotal|
    #          apply coupon -> None, (-10), (/2), Invalid
    #               |
    #           Final Total
    # var = total
    cost = 0
    cart:list = []
    subtotal = 0
    total = int
    
    for items, quant in order.items():
        if quant >= 0:
            cart.append(items)
        elif quant < 0 or quant != int:
            ValueError('Invalid quantity for <items>')

    for item in cart:
        try:
            price = prices[item]
            if price == int:
                cost = order[item] * prices[item]
                subtotal += cost
        except:
            KeyError("Unknown item: <item>")
    
            
    if coupon == None:
        total = subtotal
    elif coupon == "SAVE10":
        if subtotal < 10:
            total = 0
        else:
            total = subtotal - 10
    elif coupon == "HALF":
        total = subtotal//2
    else:
        raise ValueError("Invalid coupon")
    
    
    return total
    
            
             
        
        
    
    
    
