from django.db import models
from django.utils.timezone import localtime
import uuid
from patients.models import Patient
from cloudinary.models import CloudinaryField
from .choices import PositionChoices, StatusChoices, PrognosisChoices
from django.utils.html import mark_safe


# Create your models here.
class RetinaPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='retina_photos',
        null=False,
        blank=False,
        db_column='patient_id'
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
        folder='rrat/retina_photos',
    )
    cloudinary_public_id = models.CharField(max_length=255, blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    # Return string
    def __str__(self):
        return f"Patient: {self.patient.full_name if self.patient else 'Nobody'} --- Photo ID: {self.id}"

    class Meta:
        db_table = 'retina_photos'  
