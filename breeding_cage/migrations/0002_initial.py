# Generated by Django 4.2.6 on 2024-06-01 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("breeding_cage", "0001_initial"),
        ("mice_repository", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="breedingcage",
            name="father",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="father_breeding_cage",
                to="mice_repository.mouse",
            ),
        ),
        migrations.AddField(
            model_name="breedingcage",
            name="mother",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="mother_breeding_cage",
                to="mice_repository.mouse",
            ),
        ),
    ]
