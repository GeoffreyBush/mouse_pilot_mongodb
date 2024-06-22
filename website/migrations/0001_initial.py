# Generated by Django 5.0.6 on 2024-06-22 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mice_repository", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MouseComment",
            fields=[
                (
                    "comment_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="mice_repository.mouse",
                    ),
                ),
                (
                    "comment_text",
                    models.CharField(
                        blank=True,
                        db_column="Text",
                        default="",
                        max_length=400,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "comment",
                "managed": True,
            },
        ),
    ]
