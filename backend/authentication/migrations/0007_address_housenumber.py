# Generated by Django 4.1.7 on 2023-05-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0006_alter_user_groups_alter_user_user_permissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="housenumber",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
