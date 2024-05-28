# Generated by Django 5.0.6 on 2024-05-28 11:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mouse",
            fields=[
                ('_tube', models.IntegerField(db_column='Tube')),
                ('_global_id', models.CharField(db_column='Global ID', max_length=20, primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], db_column='Sex', default='M', max_length=1)),
                ('dob', models.DateField(db_column='Date of Birth')),
                ('clipped_date', models.DateField(blank=True, db_column='Clipped Date', null=True)),
                ('earmark', models.CharField(choices=[('', ''), ('TR', 'TR'), ('TL', 'TL'), ('BR', 'BR'), ('BL', 'BL'), ('TRTL', 'TRTL'), ('TRBR', 'TRBR'), ('TRTL', 'TRTL'), ('TLBR', 'TLBR'), ('TLBL', 'TLBL'), ('BRBL', 'BRBL')], db_column='Earmark', default='', max_length=4)),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='father_mouse', to='website.mouse')),
            ],
            options={
                "db_table": "mice",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="StockCage",
            fields=[
                (
                    "cage_id",
                    models.AutoField(
                        db_column="Cage ID", primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "db_table": "stockcage",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Strain",
            fields=[
                (
                    "strain_name",
                    models.CharField(
                        db_column="Strain",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("mice_count", models.IntegerField(db_column="Mice Count", default=0)),
            ],
            options={
                "db_table": "strain",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
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
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "user",
                "managed": True,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "comment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="website.mouse",
                    ),
                ),
                (
                    "comment_text",
                    models.CharField(
                        blank=True, db_column="Text", max_length=500, null=True
                    ),
                ),
            ],
            options={
                "db_table": "comment",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="mouse",
            name="genotyper",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="mouse",
            name="mother",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="mother_mouse",
                to="website.mouse",
            ),
        ),
        migrations.CreateModel(
            name="BreedingCage",
            fields=[
                (
                    "box_no",
                    models.CharField(
                        db_column="Box Number",
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "date_born",
                    models.DateField(
                        blank=True, db_column="DBorn", default=None, null=True
                    ),
                ),
                (
                    "number_born",
                    models.IntegerField(
                        blank=True, db_column="NBorn", default=0, null=True
                    ),
                ),
                (
                    "cull_to",
                    models.CharField(
                        blank=True,
                        db_column="C/To",
                        default="",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "date_wean",
                    models.DateField(
                        blank=True, db_column="Dwean", default=None, null=True
                    ),
                ),
                (
                    "number_wean",
                    models.CharField(
                        blank=True,
                        db_column="Nwean",
                        default="",
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "pwl",
                    models.CharField(
                        blank=True, db_column="PWL", default="", max_length=5, null=True
                    ),
                ),
                (
                    "male_pups",
                    models.IntegerField(
                        blank=True, db_column="Male Pups", default=0, null=True
                    ),
                ),
                (
                    "female_pups",
                    models.IntegerField(
                        blank=True, db_column="Female Pups", default=0, null=True
                    ),
                ),
                (
                    "transferred_to_stock",
                    models.BooleanField(db_column="Moved to Stock", default=False),
                ),
                (
                    "father",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="father_breeding_cage",
                        to="website.mouse",
                    ),
                ),
                (
                    "mother",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mother_breeding_cage",
                        to="website.mouse",
                    ),
                ),
            ],
            options={
                "db_table": "breedingcage",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "project_name",
                    models.CharField(
                        db_column="Name",
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "research_area",
                    models.CharField(
                        blank=True, db_column="Research Area", max_length=50, null=True
                    ),
                ),
                ("researchers", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                (
                    "strains",
                    models.ManyToManyField(db_column="Strain", to="website.strain"),
                ),
            ],
            options={
                "db_table": "project",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="mouse",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="website.project",
            ),
        ),
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
                ("mice", models.ManyToManyField(db_column="Mouse", to="website.mouse")),
                (
                    "researcher",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "request",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="mouse",
            name="stock_cage",
            field=models.ForeignKey(
                blank=True,
                db_column="Stock Cage ID",
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mice",
                to="website.stockcage",
            ),
        ),
        migrations.AddField(
            model_name="mouse",
            name="strain",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="website.strain"
            ),
        ),
        migrations.CreateModel(
            name="HistoricalMouse",
            fields=[
                ('_tube', models.IntegerField(db_column='Tube')),
                ('_global_id', models.CharField(db_column='Global ID', db_index=True, max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], db_column='Sex', default='M', max_length=1)),
                ('dob', models.DateField(db_column='Date of Birth')),
                ('clipped_date', models.DateField(blank=True, db_column='Clipped Date', null=True)),
                ('earmark', models.CharField(choices=[('', ''), ('TR', 'TR'), ('TL', 'TL'), ('BR', 'BR'), ('BL', 'BL'), ('TRTL', 'TRTL'), ('TRBR', 'TRBR'), ('TRTL', 'TRTL'), ('TLBR', 'TLBR'), ('TLBL', 'TLBL'), ('BRBL', 'BRBL')], db_column='Earmark', default='', max_length=4)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('father', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='website.mouse')),
                ('genotyper', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mother', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='website.mouse')),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='website.project')),
                ('stock_cage', models.ForeignKey(blank=True, db_column='Stock Cage ID', db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='website.stockcage')),
                ('strain', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='website.strain')),
            ],
            options={
                "verbose_name": "historical mouse",
                "verbose_name_plural": "historical mouses",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
