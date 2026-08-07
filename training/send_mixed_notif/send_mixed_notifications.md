# Send Mixed Notifications

Complete the notification classes and the **send_notifications** function.

Each notification type stores its delivery details and provides a *send()* method with its own output format:

-- **EmailNotification(address, subject)** returns **Email to <address>: <subject>**
-- **SMSNotification(phone_number, message)** returns **SMS to <phone_number>: <message>**
-- **PushNotification(username, message)** returns **Push for <username>: <message>**

**send_notifications(notifications)** accepts a list containing any mix of these notification objects.
Call the shared *send()* method on each object and return their results in a new list, preserving the original order.

For example:

    notifications = [
        EmailNotification("sam@example.com", "Welcome!"),
        SMSNotification("555-0102", "Your order shipped"),
    ]

    print(send_notifications(notifications))
    # ["Email to sam@example.com: Welcome!", "SMS to 555-0102: Your order shipped"]

Do not check the object's type inside **send_notifications**. Rely on the shared method name so each object chooses its own implementation.