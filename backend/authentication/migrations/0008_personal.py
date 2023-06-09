# Generated by Django 4.1.7 on 2023-06-14 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0007_address_housenumber"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nationality", models.TextField(max_length=50)),
                ("citizenship", models.TextField(max_length=50)),
                ("birthdate", models.DateTimeField()),
                ("contact_mail", models.EmailField(max_length=254)),
                ("contact_mobile", models.TextField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="personal",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
