from main import *

run_cases = [
    (
        [
            EmailNotification("sam@example.com", "Welcome!"),
            SMSNotification("555-0102", "Your order shipped"),
        ],
        [
            "Email to sam@example.com: Welcome!",
            "SMS to 555-0102: Your order shipped",
        ],
    ),
    (
        [
            PushNotification("pixel_wizard", "You have a new follower"),
            EmailNotification("lee@example.com", "Password changed"),
        ],
        [
            "Push for pixel_wizard: You have a new follower",
            "Email to lee@example.com: Password changed",
        ],
    ),
]

submit_cases = run_cases + [
    ([], []),
    (
        [SMSNotification("555-0199", "Code: 4821")],
        ["SMS to 555-0199: Code: 4821"],
    ),
    (
        [
            SMSNotification("555-0140", "Meeting at noon"),
            PushNotification("nova", "Daily reward ready"),
            EmailNotification("ada@example.com", "Weekly report"),
            PushNotification("riley", "New comment"),
        ],
        [
            "SMS to 555-0140: Meeting at noon",
            "Push for nova: Daily reward ready",
            "Email to ada@example.com: Weekly report",
            "Push for riley: New comment",
        ],
    ),
]


def describe(notification):
    if isinstance(notification, EmailNotification):
        return f'Email(address="{notification.address}", subject="{notification.subject}")'
    if isinstance(notification, SMSNotification):
        return f'SMS(phone="{notification.phone_number}", message="{notification.message}")'
    return f'Push(username="{notification.username}", message="{notification.message}")'


def test(notifications, expected):
    print("---------------------------------")
    print("Input notifications:")
    if len(notifications) == 0:
        print("  (none)")
    for notification in notifications:
        print(f"  * {describe(notification)}")
    print("")

    try:
        result = send_notifications(notifications)
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        if result == expected:
            print("Pass")
            return True
    except Exception as error:
        print(f"Error: {error}")

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
