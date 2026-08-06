def calculate_order_total(subtotal: int, customer_type: str, has_coupon: bool, shipping_method: str):
    customer = Customer(customer_type, has_coupon, shipping_method)
    member_discount = customer.calc_Mem_discount()
    coupon_discount = customer.calc_coupon_disc()
    shipping = customer.calc_ship()
    
    disc_total = subtotal - member_discount - coupon_discount
    
    if (shipping == 6 and disc_total > 75):
        shipping = 0
    order_total = subtotal - member_discount - coupon_discount + shipping
    try:
        if order_total >= 0:
            return order_total
    except:
        order_total = max(order_total, 0)
    return 0


class Customer:
    def __init__(self, customer_type: str, has_coupon: bool, shipping_method: str):
        self.customer = customer_type
        self.coupon_disc = has_coupon
        self.mem_disc = int
        self.cust_disc = int
        self.shipping = shipping_method
        self.express = "express"
        self.pickup = "pickup"
        self.standard = "standard"
        self.ship_cost = int
                
    
    def calc_Mem_discount(self) -> int:
        if self.customer == "vip":
            self.mem_disc = 20
        elif self.customer == "member":
            self.mem_disc = 10
        else:
            self.mem_disc = 0
        return self.mem_disc
    
    def calc_coupon_disc(self) -> int:
        if self.coupon_disc:
            self.cust_disc = 5
        else:
            self.cust_disc = 0
        return self.cust_disc
        
    def calc_ship(self) -> int:
        if self.shipping == self.express:
            self.ship_cost = 15
        elif self.shipping == self.pickup:
            self.ship_cost = 0
        elif self.shipping == self.standard:
            self.ship_cost = 6
        return self.ship_cost
