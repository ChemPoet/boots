def calculate_order_total(subtotal, customer_type, has_coupon, shipping_method):
    customer_discount = 0
    if customer_type == "member":
        customer_discount = 10
    elif customer_type == "vip":
        customer_discount = 20

    discounted_total = subtotal - customer_discount
    if has_coupon:
        discounted_total -= 5

    if discounted_total < 0:
        discounted_total = 0

    shipping_cost = 0
    if shipping_method == "standard" and discounted_total < 75:
        shipping_cost = 6
    elif shipping_method == "express":
        shipping_cost = 15

    return discounted_total + shipping_cost
