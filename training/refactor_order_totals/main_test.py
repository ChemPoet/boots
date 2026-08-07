from main import calculate_order_total

run_cases = [
    (80, "regular", False, "standard", 80),
    (70, "member", True, "express", 70),
]

submit_cases = run_cases + [
    (5, "vip", True, "pickup", 0),
    (105, "member", True, "standard", 90),
    (140, "vip", True, "express", 130),
]


def test(subtotal, customer_type, has_coupon, shipping_method, expected):
    print("---------------------------------")
    print(f"Subtotal:        ${subtotal}")
    print(f"Customer type:   {customer_type}")
    print(f"Has coupon:      {has_coupon}")
    print(f"Shipping method: {shipping_method}")
    print("")
    result = calculate_order_total(
        subtotal, customer_type, has_coupon, shipping_method
    )
    print(f"Expected: ${expected}")
    print(f"Actual:   ${result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
