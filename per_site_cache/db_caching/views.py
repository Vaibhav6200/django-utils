from django.shortcuts import render


def index(request):
    return render(request, 'db_caching.html')