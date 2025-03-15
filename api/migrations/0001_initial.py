# Generated by Django 5.1.7 on 2025-03-14 20:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Groups",
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
                ("group_name", models.TextField()),
                ("pwd_hash", models.TextField(null=True)),
                ("admins", models.JSONField(default=list)),
                ("banned", models.JSONField(default=list)),
                ("members", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Leaderboard",
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
                ("streak", models.IntegerField()),
                ("cards_today", models.IntegerField()),
                ("cards_month", models.IntegerField(null=True)),
                ("time_today", models.FloatField()),
                ("retention", models.FloatField(null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="League",
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
                ("xp", models.IntegerField()),
                ("time_spent", models.IntegerField()),
                ("cards", models.IntegerField()),
                ("retention", models.FloatField()),
                ("days_studied", models.FloatField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("auth_token", models.TextField(null=True)),
                ("old_hash", models.TextField(null=True)),
                ("country", models.TextField(null=True)),
                ("groups", models.JSONField(default=list, null=True)),
                ("league", models.TextField()),
                ("history", models.JSONField(default=dict, null=True)),
                ("suspended", models.TextField(null=True)),
                ("bio", models.TextField(null=True)),
                ("version", models.TextField(null=True)),
                ("sync_date", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
