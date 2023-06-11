from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Celery Testing"
        message = "This is a test mail sent"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list= [to_email],
            fail_silently=True,
        )

    return "Done"