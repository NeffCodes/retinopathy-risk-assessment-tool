from django.db import models
from django.utils.timezone import now
import uuid
from cloudinary.models import CloudinaryField

# Create your models here.
class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField(max_length=8)
    hidden = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    avatar = CloudinaryField('avatar', null=True, blank=True, folder='rrat/avatars')

    def __str__(self):
        return f"{self.full_name} - {self.id}"
        
    @property
    def age(self):
        """Returns the person's current age"""
        from datetime import date
        today = date.today()
        born = self.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age

    @property
    def full_name(self):
        """Returns the person's full name separated by a comma"""
        return f"{self.last_name}, {self.first_name}"

    @property
    def cloudinary_public_id(self):
        """Returns the public ID set for the avatar image in Cloudinary"""
        if self.date_created:
            date_str = self.date_created.strftime("%Y-%m-%d--%H:%M")
        else:
            date_str = now().strftime("%Y-%m-%d--%H:%M")
        return f"{self.last_name}-{self.first_name[0]}-{str(self.id)}-{date_str}"