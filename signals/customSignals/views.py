from django.http import HttpResponse
from . import signals


def index(request):
    signals.notification.send(sender=None, request=request, users=['vaibhav', 'jahnavi'])
    return HttpResponse("This is index Page")