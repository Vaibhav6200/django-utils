from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class EmailOTP(models.Model):
    class Meta:
        verbose_name_plural = "Email OTP"

    email = models.EmailField(max_length=255, unique=True)
    otp = models.CharField(max_length=7, blank=True, null=True)
    is_verified = models.BooleanField(default=False, help_text="if its true, that means user have verfied otp")
    datetime = models.DateTimeField(auto_now=True)


class PhoneOTP(models.Model):
    class Meta:
        verbose_name_plural = "Phone OTP"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+1112223333'. Upto 15 digits allowed.")
    # phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=7, blank=True, null=True)
    is_verified = models.BooleanField(default=False, help_text="If its true means user's account is verified")
    datetime = models.DateTimeField(auto_now=True)
