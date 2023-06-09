# Generated by Django 4.1.7 on 2023-06-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0018_alter_certificate_user_alter_education_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Health",
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
                ("allergies", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "chronic_diseases",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "medical_treatments",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("medication", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "mental_health",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("vaccines", models.TextField(blank=True, max_length=1000, null=True)),
                ("others", models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
