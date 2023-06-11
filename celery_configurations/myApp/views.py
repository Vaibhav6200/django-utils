from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func


def index(request):
    test_func.delay()
    return HttpResponse("<h1> Done </h1>")