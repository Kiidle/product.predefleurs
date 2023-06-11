# Generated by Django 4.1.7 on 2023-06-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0002_alter_task_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("Niedrig", "Niedrig"),
                    ("Mittel", "Mittel"),
                    ("Hoch", "Hoch"),
                    ("Sonderfall", "Sonderfall"),
                ],
                default="Niedrig",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("Todo", "Todo"),
                    ("In Bearbeitung", "In Bearbeitung"),
                    ("Fertig", "Fertig"),
                ],
                default="Todo",
                max_length=20,
            ),
        ),
    ]
