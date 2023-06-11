from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    # timezone.localtime(users.created_at) + timedelta(days=2)      this is how we can modify our time
    for user in users:
        mail_subject = "Celery Testing"
        message = "This is a test mail sent by scheduling a send_mail_func, it should be delivered at (9:50)"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list= [to_email],
            fail_silently=True,
        )

    return "Done"