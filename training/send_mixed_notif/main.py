# Each notification type stores its delivery details
# provides a *send()* method with its own output format

class EmailNotification:
    def __init__(self, address, subject):
        self.address = address
        self.subject = subject
    '''REDUNDANT    self.notification = (address, subject)'''
# EmailNotification(address, subject)
# returns Email to <address>: <subject>

    def send(self):
        return f"Email to {self.address}: {self.subject}"


class SMSNotification:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message
    '''REDUNDANT        self.notification = (phone_number, message)'''

# SMSNotification(phone_number, message)
# returns SMS to <phone_number>: <message>

    def send(self):
        return f"SMS to {self.phone_number}: {self.message}"


class PushNotification:
    def __init__(self, username, message):
        self.username = username
        self.message = message
    '''REDUNDANT        self.notification = (username, message)'''

# PushNotification(username, message)
# returns Push for <username>: <message>

    def send(self):
        return f"Push for {self.username}: {self.message}"


# send_notifications(notifications) accepts a list containing any mix of these notification objects
# Call the shared send() method on each object
# return their results in a new list, preserving the original order

def send_notifications(notifications: list) -> list:
    output = []
    for object in notifications:
        output.append(object.send())
    #print(output)
    return output
        

'''Do not check the object's type inside send_notifications.'''
# Rely on the shared method name so each object chooses its own implementation.