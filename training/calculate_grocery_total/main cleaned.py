def calculate_total(order: dict[str, int], prices: dict[str, int], coupon=None):
    
    cost = 0
    cart:list = []
    subtotal = 0
    total = int
    
    for key, value in order.items():
        if value > 0:
            cart.append(key)
        elif value < 0:
            raise ValueError(f"Invalid quantity for '{key}'")

    for item in cart:
        try:
            if prices[item] >= 0:
                cost = order[item] * prices[item]
                subtotal += cost
        except:
            raise KeyError(f"Unknown item: '{item}'")
    

    if coupon == None:
        total = subtotal
    elif coupon == "SAVE10":
        total = max(0, subtotal - 10)
    elif coupon == "HALF":
        total = subtotal//2
    else:
        raise ValueError("Invalid coupon")
    
    
    return total
    
            
             
        
        
    
    
    
