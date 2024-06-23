# Generated by Django 5.0.6 on 2024-06-23 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mice_repository', '0001_initial'),
        ('strain', '0001_initial'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreedingCage',
            fields=[
                ('cagemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.cagemodel')),
                ('date_born', models.DateField(blank=True, db_column='DBorn', default=None, null=True)),
                ('number_born', models.IntegerField(blank=True, db_column='NBorn', default=0, null=True)),
                ('cull_to', models.CharField(blank=True, db_column='C/To', default='', max_length=20, null=True)),
                ('date_wean', models.DateField(blank=True, db_column='Dwean', default=None, null=True)),
                ('number_wean', models.CharField(blank=True, db_column='Nwean', default='', max_length=5, null=True)),
                ('pwl', models.CharField(blank=True, db_column='PWL', default='', max_length=5, null=True)),
                ('male_pups', models.IntegerField(blank=True, db_column='Male Pups', default=0, null=True)),
                ('female_pups', models.IntegerField(blank=True, db_column='Female Pups', default=0, null=True)),
                ('transferred_to_stock', models.BooleanField(db_column='Moved to Stock', default=False)),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cage_father', to='mice_repository.mouse')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cage_mother', to='mice_repository.mouse')),
                ('strain', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='strain.strain')),
            ],
            options={
                'db_table': 'breedingcage',
                'managed': True,
            },
            bases=('website.cagemodel',),
        ),
    ]
