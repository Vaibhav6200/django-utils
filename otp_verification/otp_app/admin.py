from django.contrib import admin
from .models import *


class CustomEmailOTP(admin.ModelAdmin):
    list_display = ['id', 'email', 'otp', 'is_verified', 'datetime']
    list_display_links = ['id', 'email', 'otp', 'is_verified', 'datetime']


class CustomPhoneOTP(admin.ModelAdmin):
    list_display = ['id', "user", "phone", "otp", "is_verified", "datetime"]
    list_display_links = ['id', "user"
                          ]
admin.site.register(EmailOTP, CustomEmailOTP)
admin.site.register(PhoneOTP, CustomPhoneOTP)