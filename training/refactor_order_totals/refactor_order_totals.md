# Refactor Order Totals

The *calculate_order_total* function calculates a discounted order total, including shipping. Its current implementation repeats calculations and produces incorrect totals for some combinations.

Refactor the function so that each discount and shipping rule is handled once while preserving its public interface.


# Rules
-   Members receive a _$10_ discount.
-   VIP customers receive a _$20_ discount.
-   Regular customers receive no customer discount.
-   A valid coupon subtracts another _$5_.
-   The discounted order total cannot be less than _0_.
-   Pickup is free.
-   Standard shipping costs _$6_, but is free when the discounted total is at least _$75_.
-   Express shipping always costs _$15_.

**All inputs use a valid customer type and shipping method.**

# Example
    calculate_order_total(70, "member", True, "express")
    # 70 - 10 - 5 + 15 = 70

Remove redundant temporary values, repeated condition checks, and duplicated calculations while ensuring all tests pass.

# Notes
    --use classes, objects, and methods with private variable instances
    --ID repeating patterns of code to set as class/object
    -- subtotal: int
    -- customer_type: str (ALWAYS VALID)
    -- has_coupon: bool
    -- shipping_method: str (ALWAYS VALID)
    -- discounted_total !< 0
