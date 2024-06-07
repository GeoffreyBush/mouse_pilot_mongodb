# Generated by Django 5.0.6 on 2024-06-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mice_repository", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "request_id",
                    models.AutoField(db_column="ID", primary_key=True, serialize=False),
                ),
                (
                    "task_type",
                    models.CharField(
                        choices=[
                            ("Cl", "Clip"),
                            ("Cu", "Cull"),
                            ("Mo", "Move"),
                            ("We", "Wean"),
                        ],
                        default="Cl",
                        max_length=2,
                    ),
                ),
                ("confirmed", models.BooleanField(default=False)),
                (
                    "new_message",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "message_history",
                    models.CharField(blank=True, max_length=10000, null=True),
                ),
                (
                    "mice",
                    models.ManyToManyField(
                        db_column="Mouse", to="mice_repository.mouse"
                    ),
                ),
            ],
            options={
                "db_table": "request",
                "managed": True,
            },
        ),
    ]
