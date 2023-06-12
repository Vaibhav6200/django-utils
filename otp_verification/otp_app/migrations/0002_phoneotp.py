# Generated by Django 4.2.2 on 2023-06-12 08:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+1112223333'. Upto 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('otp', models.CharField(blank=True, max_length=7, null=True)),
                ('is_verified', models.BooleanField(default=False, help_text="If its true means user's account is verified")),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Phone OTP',
            },
        ),
    ]
