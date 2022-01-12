from django.dispatch import Signal, receiver


#create signals
notification = Signal()


#reciever function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notifications")
        