# Generated by Django 1.11.2 on 2017-12-19 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import qsessions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name="session key"),
                ),
                ("session_data", models.TextField(verbose_name="session data")),
                ("expire_date", models.DateTimeField(db_index=True, verbose_name="expire date")),
                ("user_agent", models.CharField(blank=True, max_length=300, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("ip", models.GenericIPAddressField(blank=True, null=True, verbose_name="IP")),
                (
                    "user",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={"verbose_name": "session", "abstract": False, "verbose_name_plural": "sessions"},
            managers=[("objects", qsessions.models.SessionManager())],
        ),
    ]
