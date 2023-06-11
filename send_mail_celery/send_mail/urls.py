from django.urls import path
from . import views


app_name="send_mail"

urlpatterns = [
    path('', views.index, name="index"),
    path('mailAll/', views.send_mail_to_all, name="mailAll"),
]