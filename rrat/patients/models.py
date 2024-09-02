from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    date_of_birth = models.DateField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.age}"
        
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