# Generated by Django 4.1.7 on 2023-05-17 11:29

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "pp",
                    models.ImageField(
                        blank=True, null=True, upload_to="static/images/uploads/profile"
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="authentication_user_set",
                        to="auth.group",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="authentication_user_set",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Warn",
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
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("Falschinformationen", "Falschinformationen"),
                            (
                                "Missbrauch von Privilegien",
                                "Missbrauch von Privilegien",
                            ),
                            ("Belästigung", "Belästigung"),
                            ("Cybermobbing", "Cybermobbing"),
                            ("Cybergrooming", "Cybergrooming"),
                            ("Whataboutismus", "Whataboutismus"),
                            ("Relativierung", "Relativierung"),
                            ("Erpressung", "Erpressung"),
                            ("Drohung", "Drohung"),
                            ("Wortwahl", "Wortwahl"),
                            ("Hassrede", "Hassrede"),
                            ("Beleidugung", "Beleidigung"),
                            ("Diskriminierung", "Diskriminierung"),
                            ("Sexismus", "Sexismus"),
                            ("Rassismus", "Rassismus"),
                            ("Faschismus", "Faschismus"),
                            ("Antisemitismus", "Antisemitismus"),
                            ("Betrug", "Betrug"),
                            ("Spam", "Spam"),
                        ],
                        default="Hassrede",
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="warns",
                        to="authentication.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Data",
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
                ("verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data",
                        to="authentication.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                (
                    "country",
                    models.CharField(choices=[("Schweiz", "Schweiz")], max_length=50),
                ),
                (
                    "canton",
                    models.CharField(
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
                ("location", models.CharField(max_length=50)),
                ("postalcode", models.IntegerField(default=0)),
                ("street", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="authentication.user",
                    ),
                ),
            ],
        ),
    ]
