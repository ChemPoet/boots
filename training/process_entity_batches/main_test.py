from main import *

run_cases = [
    (
        [
            {"action": "create", "entity": Material("mat-1", "Steel", 12)},
            {"action": "create", "entity": Machine("mac-1", "Press", 84)},
            {"action": "summary"},
        ],
        [
            {"ok": True, "action": "create", "id": "mat-1"},
            {"ok": True, "action": "create", "id": "mac-1"},
            {
                "ok": True,
                "action": "summary",
                "summary": {
                    "total": 2,
                    "materials": 1,
                    "machines": 1,
                    "material_units": 12,
                    "average_machine_condition": 84,
                },
            },
        ],
    ),
    (
        [
            {"action": "create", "entity": Machine("mac-2", "Lathe", 70)},
            {"action": "update", "id": "mac-2", "changes": {"name": "CNC Lathe", "condition": 92}},
            {"action": "remove", "id": "mac-2"},
            {"action": "summary"},
        ],
        [
            {"ok": True, "action": "create", "id": "mac-2"},
            {"ok": True, "action": "update", "id": "mac-2"},
            {"ok": True, "action": "remove", "id": "mac-2"},
            {
                "ok": True,
                "action": "summary",
                "summary": {"total": 0, "materials": 0, "machines": 0, "material_units": 0, "average_machine_condition": 0},
            },
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            {"action": "create", "entity": Material("mat-3", "Bolts", 20)},
            {"action": "create", "entity": Material("mat-3", "Nuts", 10)},
            {"action": "update", "id": "missing", "changes": {"quantity": 4}},
            {"action": "archive", "id": "mat-3"},
            {"action": "summary"},
        ],
        [
            {"ok": True, "action": "create", "id": "mat-3"},
            {"ok": False, "action": "create", "error": "duplicate entity: mat-3"},
            {"ok": False, "action": "update", "error": "entity not found: missing"},
            {"ok": False, "action": "archive", "error": "unknown action: archive"},
            {"ok": True, "action": "summary", "summary": {"total": 1, "materials": 1, "machines": 0, "material_units": 20, "average_machine_condition": 0}},
        ],
    ),
    (
        [
            {"action": "create", "entity": Material("mat-4", "Wire", 8)},
            {"action": "update", "id": "mat-4", "changes": {"quantity": -1}},
            {"action": "update", "id": "mat-4", "changes": {"condition": 50}},
            {"action": "update", "id": "mat-4", "changes": {"name": "Copper Wire", "quantity": 16}},
            {"action": "summary"},
        ],
        [
            {"ok": True, "action": "create", "id": "mat-4"},
            {"ok": False, "action": "update", "error": "invalid quantity"},
            {"ok": False, "action": "update", "error": "unknown field: condition"},
            {"ok": True, "action": "update", "id": "mat-4"},
            {"ok": True, "action": "summary", "summary": {"total": 1, "materials": 1, "machines": 0, "material_units": 16, "average_machine_condition": 0}},
        ],
    ),
    (
        [
            {"action": "create", "entity": Material("mat-5", "Panels", 30)},
            {"action": "create", "entity": Material("mat-6", "Screws", 120)},
            {"action": "create", "entity": Machine("mac-5", "Cutter", 80)},
            {"action": "create", "entity": Machine("mac-6", "Welder", 91)},
            {"action": "update", "id": "mat-5", "changes": {"quantity": 45}},
            {"action": "remove", "id": "mat-6"},
            {"action": "summary"},
        ],
        [
            {"ok": True, "action": "create", "id": "mat-5"},
            {"ok": True, "action": "create", "id": "mat-6"},
            {"ok": True, "action": "create", "id": "mac-5"},
            {"ok": True, "action": "create", "id": "mac-6"},
            {"ok": True, "action": "update", "id": "mat-5"},
            {"ok": True, "action": "remove", "id": "mat-6"},
            {"ok": True, "action": "summary", "summary": {"total": 3, "materials": 1, "machines": 2, "material_units": 45, "average_machine_condition": 85}},
        ],
    ),
]


def describe_operation(operation):
    action = operation.get("action")
    if action == "create":
        entity = operation["entity"]
        details = f"id={entity.entity_id}, name={entity.name}"
        if isinstance(entity, Material):
            details += f", quantity={entity.quantity}"
        else:
            details += f", condition={entity.condition}"
        return f"create {entity.__class__.__name__}({details})"
    if action == "update":
        return f"update id={operation['id']}, changes={operation['changes']}"
    if action == "remove":
        return f"remove id={operation['id']}"
    return str(action)


def test(operations, expected):
    print("---------------------------------")
    print("Input operations:")
    for operation in operations:
        print(f"  - {describe_operation(operation)}")

    processor = BatchProcessor(EntityCollection())
    actual = processor.process(operations)

    print("\nExpected:")
    for result in expected:
        print(f"  {result}")
    print("Actual:")
    for result in actual:
        print(f"  {result}")

    if actual == expected:
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
