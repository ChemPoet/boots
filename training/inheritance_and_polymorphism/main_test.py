from main import Spell, FireSpell, IceSpell, cast_all

run_cases = [
    (
        [FireSpell("Flame Burst", 20), IceSpell("Frost Bite", 15)],
        30,
        [
            "Fire spell 'Flame Burst' hits for 40 damage!",
            "Ice spell 'Frost Bite' hits for 35 damage!",
        ],
    ),
    (
        [FireSpell("Inferno", 50)],
        25,
        [
            "Fire spell 'Inferno' hits for 35 damage!",
        ],
    ),
    (
        [],
        10,
        [],
    ),
]

submit_cases = run_cases + [
    (
        [IceSpell("Glacier Spike", 40)],
        15,
        [
            "Ice spell 'Glacier Spike' hits for 20 damage!",
        ],
    ),
    (
        [
            FireSpell("Ember", 5),
            FireSpell("Blaze", 15),
            IceSpell("Snowball", 3),
        ],
        10,
        [
            "Fire spell 'Ember' hits for 20 damage!",
            "Fire spell 'Blaze' hits for 20 damage!",
            "Ice spell 'Snowball' hits for 15 damage!",
        ],
    ),
    (
        [
            IceSpell("Hail Storm", 30),
            IceSpell("Frozen Lance", 25),
        ],
        50,
        [
            "Ice spell 'Hail Storm' hits for 55 damage!",
            "Ice spell 'Frozen Lance' hits for 55 damage!",
        ],
    ),
]


def describe_spells(spells):
    if not spells:
        return "  (no spells)"
    lines = []
    for spell in spells:
        cls_name = spell.__class__.__name__
        name = getattr(spell, "name", None)
        mana_cost = getattr(spell, "mana_cost", None)
        lines.append(
            f"  - {cls_name}(name='{name}', mana_cost={mana_cost})"
        )
    return "\n".join(lines)


def test(spells, base_power, expected_output):
    print("---------------------------------")
    print("Input:")
    print("Spells:")
    print(describe_spells(spells))
    print(f"Base power: {base_power}")
    print("")
    result = cast_all(spells, base_power)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
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
