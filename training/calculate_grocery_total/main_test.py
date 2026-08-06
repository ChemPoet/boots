from main import calculate_total


def format_input(order, prices, coupon):
    lines = ["Input:"]
    lines.append("  Order:")
    if not order:
        lines.append("    (empty)")
    else:
        for k in sorted(order.keys()):
            lines.append(f"    - {k}: {order[k]}")
    lines.append("  Prices:")
    if not prices:
        lines.append("    (empty)")
    else:
        for k in sorted(prices.keys()):
            lines.append(f"    - {k}: {prices[k]}")
    lines.append(f"  Coupon: {coupon}")
    return "\n".join(lines)


def run_test_case(order, prices, coupon, expected=None, expect_error=False, error_type=None, error_msg_substr=None):
    print("---------------------------------")
    print(format_input(order, prices, coupon))
    try:
        result = calculate_total(order, prices, coupon)
        if expect_error:
            print("Expected: raise {0}".format(error_type.__name__ if error_type else "<error>"))
            print(f"Actual:   returned {result}")
            print("Fail")
            return False
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        if result == expected:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        if not expect_error:
            print(f"Expected: {expected}")
            print(f"Actual:   raised {type(e).__name__}: {e}")
            print("Fail")
            return False
        matches_type = (error_type is None) or isinstance(e, error_type)
        matches_msg = (error_msg_substr is None) or (error_msg_substr in str(e))
        print(f"Expected: raise {error_type.__name__ if error_type else '<error>'} (message contains: {error_msg_substr})")
        print(f"Actual:   raised {type(e).__name__}: {e}")
        if matches_type and matches_msg:
            print("Pass")
            return True
        print("Fail")
        return False


# Happy-path run cases
run_cases = [
    ({"apple": 2, "banana": 3}, {"apple": 4, "banana": 2}, None, 14),
    ({"milk": 1, "bread": 1}, {"milk": 5, "bread": 3}, "SAVE10", 0),
]

# Submit cases: begin with a happy path, include edge/error cases, end with a big happy path
submit_cases = [
    # Happy path
    {"order": {"rice": 3}, "prices": {"rice": 7}, "coupon": "HALF", "expected": 10},
    # Invalid quantity (negative)
    {"order": {"eggs": -1}, "prices": {"eggs": 2}, "coupon": None, "expect_error": True, "error_type": ValueError, "error_msg_substr": "Invalid quantity for 'eggs'"},
    # Unknown item in prices
    {"order": {"cheese": 2}, "prices": {"bread": 3}, "coupon": None, "expect_error": True, "error_type": KeyError, "error_msg_substr": "Unknown item: 'cheese'"},
    # Invalid coupon
    {"order": {"apple": 1}, "prices": {"apple": 4}, "coupon": "BOGO", "expect_error": True, "error_type": ValueError, "error_msg_substr": "Invalid coupon"},
    # Big happy path
    {"order": {"apple": 4, "banana": 5, "milk": 2, "bread": 3}, "prices": {"apple": 3, "banana": 2, "milk": 5, "bread": 3}, "coupon": None, "expected": 4*3 + 5*2 + 2*5 + 3*3},
]


def main():
    # Build test list depending on environment
    test_cases = []
    if "__RUN__" in globals():
        # Convert run_cases tuples to dicts consistent with submit handler
        for (o, p, c, exp) in run_cases:
            test_cases.append({"order": o, "prices": p, "coupon": c, "expected": exp})
    else:
        test_cases = submit_cases

    passed = 0
    failed = 0

    for tc in test_cases:
        correct = run_test_case(
            tc.get("order", {}),
            tc.get("prices", {}),
            tc.get("coupon", None),
            expected=tc.get("expected"),
            expect_error=tc.get("expect_error", False),
            error_type=tc.get("error_type"),
            error_msg_substr=tc.get("error_msg_substr"),
        )
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    skipped = 0
    if "__RUN__" in globals():
        skipped = len(submit_cases) - len(run_cases)
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


main()
