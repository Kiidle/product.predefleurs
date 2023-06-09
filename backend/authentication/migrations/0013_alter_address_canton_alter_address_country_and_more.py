# Generated by Django 4.1.7 on 2023-06-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0012_alter_personal_contact_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="canton",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Aargau", "Aargau"),
                    ("Appenzell Ausserrhoden", "Appenzell Ausserrhoden"),
                    ("Appenzell Innerrhoden", "Appenzell Innerrhoden"),
                    ("Basel-Landschaft", "Basel-Landschaft"),
                    ("Basel-Stadt", "Basel-Stadt"),
                    ("Bern", "Bern"),
                    ("Freiburg", "Freiburg"),
                    ("Genf", "Genf"),
                    ("Glarus", "Glarus"),
                    ("Graubünden", "Graubünden"),
                    ("Jura", "Jura"),
                    ("Luzern", "Luzern"),
                    ("Neuenburg", "Neuenburg"),
                    ("Nidwalden", "Nidwalden"),
                    ("Obwalden", "Obwalden"),
                    ("St. Gallen", "St. Gallen"),
                    ("Schaffhausen", "Schaffhausen"),
                    ("Schwyz", "Schwyz"),
                    ("Solothurn", "Solothurn"),
                    ("Thurgau", "Thurgau"),
                    ("Tessin", "Tessin"),
                    ("Uri", "Uri"),
                    ("Wallis", "Wallis"),
                    ("Waadt", "Waadt"),
                    ("Zug", "Zug"),
                    ("Zürich", "Zürich"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="country",
            field=models.CharField(
                blank=True, choices=[("Schweiz", "Schweiz")], max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="housenumber",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="address",
            name="location",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="address",
            name="postalcode",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
