# Generated by Django 4.1.7 on 2023-06-14 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0016_remove_user_registration_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("start", models.DateField()),
                ("end", models.DateField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Lehre", "lehre"),
                            ("Berufsmaturität", "berufsmaturität"),
                            ("Fachmaturität", "fachmaturität"),
                            ("Bachelor-Studium", "bachelor"),
                            ("Master-Studium", "master"),
                            ("Diplomstudium", "diplomstudium"),
                            ("Höhere Fachschule", "hf"),
                            ("Fachhochschule", "Fachhochschule"),
                            ("Universität", "Universität"),
                        ],
                        max_length=50,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("institution", models.CharField(max_length=50)),
                ("specialization", models.CharField(max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, max_length=200, null=True),
                ),
                ("final_grade", models.CharField(blank=True, max_length=5, null=True)),
                ("grades", models.TextField(blank=True, max_length=200, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
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
                ("title", models.CharField(max_length=50)),
                ("issuer", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("expiration", models.DateField()),
                ("certificatenumber", models.IntegerField()),
                ("description", models.TextField(max_length=200)),
                ("level", models.CharField(max_length=10)),
                ("reference", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certificates",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]