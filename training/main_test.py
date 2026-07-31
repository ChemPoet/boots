from main import *

run_cases = [
    (["ana", "bo", "ana", "cy", "bo", "ana"], ["ana", "bo"]),
    (["kai", "mira", "sol"], []),
    (["ivy", "ivy", "leo", "mira", "leo"], ["ivy", "leo"]),
]

submit_cases = run_cases + [
    ([], []),
    (["zoe", "zoe", "zoe", "zoe"], ["zoe"]),
    (["rex", "nova", "rex", "pix", "nova", "luna", "pix"], ["rex", "nova", "pix"]),
]


def test(usernames, expected_output):
    print("---------------------------------")
    print(f"Input: {usernames}")
    print("")
    result = find_repeated_usernames(usernames)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False



def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
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
