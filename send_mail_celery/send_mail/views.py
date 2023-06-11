from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_func

def index(request):
    return HttpResponse("<h1>Hii Vaibhav</h1>")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("<h2>Mails are sent by Celery</h2>")