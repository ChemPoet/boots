from main import *

run_cases = [
    (
        "add",
        (("potion", 3), ("torch", 5)),
        ("rope", 2),
        (("potion", 3), ("torch", 5), ("rope", 2)),
    ),
    (
        "change",
        (("arrow", 12), ("bread", 4)),
        ("arrow", 20),
        (("arrow", 20), ("bread", 4)),
    ),
]

submit_cases = run_cases + [
    (
        "remove",
        (("map", 1), ("coin", 30)),
        ("key",),
        (("map", 1), ("coin", 30)),
    ),
    (
        "add",
        (("potion", 3),),
        ("potion", 99),
        (("potion", 3),),
    ),
    (
        "remove",
        (("sword", 1), ("shield", 1), ("apple", 6)),
        ("shield",),
        (("sword", 1), ("apple", 6)),
    ),
]


def test(operation, inventory, arguments, expected):
    print("---------------------------------")
    print(f"Operation: {operation}")
    print(f"Input inventory: {inventory}")
    print(f"Arguments: {arguments}")
    print("")

    original_snapshot = tuple(inventory)

    if operation == "add":
        result = add_item(inventory, *arguments)
    elif operation == "change":
        result = change_quantity(inventory, *arguments)
    else:
        result = remove_item(inventory, *arguments)

    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    print(f"Original unchanged: {inventory == original_snapshot}")
    print(f"Result is a tuple:  {isinstance(result, tuple)}")

    if (
        result == expected
        and inventory == original_snapshot
        and isinstance(result, tuple)
    ):
        print("Pass")
        return True

    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        if test(*test_case):
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
