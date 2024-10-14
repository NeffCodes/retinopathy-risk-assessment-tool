from django.db import models
import uuid

# Create your models here.
class RetinaPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    
    def __str__(self):
        return self.id