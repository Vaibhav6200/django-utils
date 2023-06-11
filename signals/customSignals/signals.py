from django.dispatch import receiver, Signal

notification = Signal()

@receiver(notification)
def notif_receiver(sender, **kwargs):
    print("Inside Notification Receiver, triggers when we send a signal")
    print(f"sender: {sender}")
    print(f"kwargs: {kwargs}")