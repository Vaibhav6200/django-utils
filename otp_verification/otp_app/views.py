import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .helper import *
from .models import *


class PhoneOTPSend(APIView):
    def post(self, request):        # required = phone
        serializer = PhoneOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = "+91" + request.data['phone']
            MessageHandler(phone_number).send_otp_via_message()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneOTPVerify(APIView):
    def put(self, request):    # request has "phone" and "otp"
        phone_number = "+91" + request.data['phone']
        user_entered_otp = request.data['otp']
        try:
            verify = MessageHandler(phone_number).verify_message_otp(user_entered_otp)
            if verify == "approved":
                return Response({"message": "OTP Verified Successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "OTP Verified Failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "OTP Verified Failed"}, status=status.HTTP_400_BAD_REQUEST)


class EmailOTPSend(APIView):
    def post(self, request):
        serializer = EmailOTPSerializer(data=request.data)
        if serializer.is_valid():
            otp = random.randint(1000000, 9999999)
            serializer.save(otp=f"{otp}")
            EmailHandler(request.data['email'], otp).send_otp_via_mail()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailOTPVerify(APIView):
    def put(self, request):
        email_model = EmailOTP.objects.get(email=request.data['email'])
        if email_model.otp == request.data['otp']:
            email_model.is_verified=True
            email_model.save()
            return Response({"message": "OTP verified Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "OTP verified Failed"}, status=status.HTTP_400_BAD_REQUEST)
