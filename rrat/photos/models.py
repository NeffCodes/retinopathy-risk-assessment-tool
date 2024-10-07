from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class RetinaPhoto(models.Model):
    LEFT = 'left'
    RIGHT = 'right'
    POSITION_CHOICES = [ (LEFT, 'Left'), (RIGHT, 'Right') ]

    # user = models.ForeignKey() ## TODO add foreign key once users set up
    title = models.CharField(max_length=255)
    image = CloudinaryField('image', folder='rrat/retina_scans')
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.position}: {self.date_created}"