from django.db import models
import uuid
from patients.models import Patient
from cloudinary.models import CloudinaryField
from choices import *

# Create your models here.
class RetinaPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,       # Will remove all photos tied to a patient if the patient is deleted
        related_name='retina_photos',   # Allows accessing all photo scans related to a patient via patient.photo_scans.all()
        null=False,                     # Makes it so a photo can not exist without a patient
        blank=False,                    # Makes it so the form can not save ntil a patient is set
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    position = models.CharField(
        max_length=5, 
        choices=PositionChoices.choices
    )
    status = models.CharField(
        max_length=20, 
        choices=StatusChoices.choices, 
        default=StatusChoices.UNPROCESSED
    )
    prognosis = models.CharField(
        max_length=20, 
        choices=PrognosisChoices.choices, 
        default=None,
        null=True,
        blank=True
    )
    image = CloudinaryField(
        'image', 
        null=False, 
        blank=False, 
        folder='rrat/retina_photos'
    )
    cloudinary_public_id = ""

    def __str__(self):
        return self.id