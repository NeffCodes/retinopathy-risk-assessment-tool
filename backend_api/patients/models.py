  from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100) #stores the patient's name up to 100 char max
    dob = models.DateField() #Patient's DOB
    history = models.TextField() #Patient's medical hx or diabetes dx...may change to uniique ID in place of this  though

    def __str__(self):
        return self.name

