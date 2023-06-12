from rest_framework import serializers
from .models import *


class EmailOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOTP
        fields = "__all__"


class PhoneOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneOTP
        fields = "__all__"