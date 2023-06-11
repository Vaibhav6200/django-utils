from django.urls import path
from . import views


app_name="send_mail"

urlpatterns = [
    path('', views.index, name="index"),
    path('mail_all/', views.send_mail_to_all, name="mailAll"),
    path('schedule_mail/', views.schedule_mail, name="schedule_mail"),
]