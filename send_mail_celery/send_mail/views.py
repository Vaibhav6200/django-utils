from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def index(request):
    return HttpResponse("<h1>Hii Vaibhav</h1>")

def send_mail_to_all(request):
    # send_mail_func.delay()        # statically sending mail
    return HttpResponse("<h2>Mails are sent by Celery</h2>")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=23, minute=3)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_2", task="send_mail.tasks.send_mail_func")
    return HttpResponse("<h1>Schedule Done </h1>")