from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    otp = models.CharField(max_length=7, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

