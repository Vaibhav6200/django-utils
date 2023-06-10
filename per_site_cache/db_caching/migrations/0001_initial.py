# Generated by Django 4.2.2 on 2023-06-08 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbCaching',
            fields=[
                ('cache_key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'db_caching',
            },
        ),
    ]
