from django.urls import path
from . import views

app_name = 'otp_app'

urlpatterns = [
    path('send_mail/', views.EmailOTPSend.as_view()),
    path('verify_mail/', views.EmailOTPVerify.as_view()),
    path('send_phone/', views.PhoneOTPSend.as_view()),
    path('verify_phone/', views.PhoneOTPVerify.as_view()),
]
