# Generated by Django 4.2.6 on 2024-06-01 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("website", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="researchers",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="project",
            name="strains",
            field=models.ManyToManyField(db_column="Strain", to="website.strain"),
        ),
    ]
