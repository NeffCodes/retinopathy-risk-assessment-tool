from django.contrib import admin
from .models import Patient as PatientModel

class PatientModelAdmin(admin.ModelAdmin):
    # What shows up on the admin panel list
    list_display = ("id","first_name","last_name","hidden","date_created","date_updated", 'avatar')

    # what shows up when you edit or add a patient via the admin panel
    fields = ("first_name","last_name","date_of_birth","hidden", "avatar")

# Register your models here.
admin.site.register(PatientModel, PatientModelAdmin)