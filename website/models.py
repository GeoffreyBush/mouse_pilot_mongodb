from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

from website.constants import EARMARK_CHOICES_PAIRED

""" DANGER ZONE """
""" Editing this file affects the database """

# It's preferred not to set null=True for CharField and TextField, use empty string (default value) or blank instead,
# or raise ValidationError for empty input


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        managed = True
        db_table = "user"


class Mice(models.Model):

    sex = models.CharField(
        db_column="Sex",
        max_length=1,
        default="M",
        choices=[("M", "Male"), ("F", "Female")],
        null=False,
    )
    dob = models.DateField(db_column="Date of Birth", null=False)
    clippedDate = models.DateField(db_column="Clipped Date", null=True, blank=True)
    genotyped = models.BooleanField(db_column="Genotyped", null=False)
    # Culled boolean attribute will be useful

    #########################
    # Foreign keys for Mice #
    #########################
    mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mother_mice",
    )
    father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="father_mice",
    )

    # Should be either stock cage or experimental cage
    """
    cage = models.ForeignKey(
        "Cage", models.SET_NULL, db_column="Cage ID", null=True, blank=True
    )
    """

    project = models.ForeignKey(
        "Project", on_delete=models.SET_NULL, null=True, blank=True
    )
    genotyper = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL, null=True, blank=True
    )
    strain = models.ForeignKey(
        "Strain", on_delete=models.SET_NULL, blank=True, null=True
    )
    earmark = models.CharField(
        db_column="Earmark",
        max_length=4,
        default="",
        choices=EARMARK_CHOICES_PAIRED,
        null=False,
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = "mice"


class Request(models.Model):

    TASK_CHOICES = [
        ("Cl", "Clip"),
        ("Cu", "Cull"),
        ("Mo", "Move"),
        ("We", "Wean"),
    ]

    request_id = models.AutoField(db_column="ID", primary_key=True)
    researcher = models.ForeignKey(
        "CustomUser", on_delete=models.SET_NULL, null=True, blank=True
    )
    task_type = models.CharField(max_length=2, choices=TASK_CHOICES, default="Cl")
    mice = models.ManyToManyField("Mice", db_column="Mice")
    confirmed = models.BooleanField(
        default=False
    )  # confirmed attribute could be switched to flag with choices?
    new_message = models.CharField(max_length=1000, null=True, blank=True)
    message_history = models.CharField(max_length=10000, null=True, blank=True)

    def confirm(self):
        if not self.confirmed:
            self.confirmed = True
            self.save()

            if self.task_type == "Cl":
                for mouse in self.mice.all():
                    mouse.genotyped = True
                    mouse.save()
                    # need to prompt user for earmark vefore clipping is confirmed

            # Add other task types here

    def __str__(self):
        return f"{self.request_id}"

    class Meta:
        managed = True
        db_table = "request"


class Comment(models.Model):

    # Comment ID primary key is derived from Mice ID primary key
    comment = models.OneToOneField("Mice", on_delete=models.CASCADE, primary_key=True)

    # Django forces you to set a max_length property. Not sure if 500 characters is too much/enough.
    comment_text = models.CharField(
        db_column="Text", max_length=500, null=True, blank=True
    )

    def __str__(self):
        return f"{self.comment_id}"

    class Meta:
        managed = True
        db_table = "comment"


################################################
# Models needed as foreign keys for Mice model #
################################################


class Strain(models.Model):
    strain_name = models.CharField(db_column="Strain", primary_key=True, max_length=20)

    def __str__(self):
        return f"{self.strain_name}"

    class Meta:
        managed = True
        db_table = "strain"


class Project(models.Model):
    projectname = models.CharField(db_column="Name", primary_key=True, max_length=30)
    researcharea = models.CharField(
        db_column="Research Area", max_length=50, null=True, blank=True
    )
    strains = models.ManyToManyField("Strain", db_column="Strain")
    researchers = models.ManyToManyField(CustomUser)
    mice_count = 0

    def __str__(self):
        return f"{self.projectname}"

    class Meta:
        managed = True
        db_table = "project"


# assume this to be the breeding cage
class BreedingCage(models.Model):

    cageID = models.AutoField(db_column="Cage ID", primary_key=True)
    box_no = models.CharField(
        db_column="Box Number", max_length=10, null=False, blank=False
    )
    # the status of the cage
    status = models.CharField(
        db_column="Status",
        max_length=20,
        default="Empty",
        choices=[
            ("Empty", "Empty"),
            ("ParentsInside", "ParentsInside"),
            ("ParentsRemoved", "ParentsRemoved"),
        ],
        null=False,
    )
    mother = models.CharField(db_column="Mother", max_length=20, null=True, blank=True)
    father = models.CharField(db_column="Father", max_length=20, null=True, blank=True)
    date_born = models.DateField(db_column="DBorn", null=False)
    number_born = models.CharField(
        db_column="NBorn", max_length=5, null=True, blank=True
    )
    cull_to = models.CharField(db_column="C/To", max_length=20, null=True, blank=True)
    date_wean = models.DateField(db_column="Dwean", null=False)
    number_wean = models.CharField(
        db_column="Nwean", max_length=5, null=True, blank=True
    )
    pwl = models.CharField(db_column="PWL", max_length=5, null=True, blank=True)

    def __str__(self):
        return f"{self.cageID}"

    class Meta:
        managed = True
        db_table = "breedingcage"
