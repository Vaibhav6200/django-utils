from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings


class MessageHandler:
    phone_number = None

    auth_token = settings.AUTH_TOKEN
    account_sid = settings.ACCOUNT_SID
    verify_sid = settings.VERIFY_SID

    def __init__(self, phone=None):
        self.phone_number = phone

    def send_otp_via_message(self):
        client = Client(self.account_sid, self.auth_token)
        verification = client.verify.v2.services(self.verify_sid).verifications.create(to=self.phone_number, channel="sms")
        print(verification.status)

    def verify_message_otp(self, otp):
        client = Client(self.account_sid, self.auth_token)
        verification_check = client.verify.v2.services(self.verify_sid).verification_checks.create(to=self.phone_number, code=otp)
        print("**********************")
        print(verification_check.status)
        print("**********************")
        return verification_check.status


class EmailHandler:
    otp = None
    email = None

    def __init__(self, email, otp) -> None:
        self.email = email
        self.otp = otp

    def send_otp_via_mail(self):
        subject = "OTP Verification"
        message = f"Your OTP is {self.otp}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        send_mail(subject, message, from_email, recipient_list)

