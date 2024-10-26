from django.contrib import admin
from .models import RetinaPhoto as RetinaPhotoModel

class RetinaPhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("image","position","cloudinary_public_id", 'image_tag')

    # What shows up on the admin panel list
    list_display = ("patient_name", "position", "cloudinary_public_id")

    # what shows up when you edit or add a patient via the admin panel
    fields = ("patient", "image", "position", "cloudinary_public_id", "image_tag")

    # Pull the name of the patient through the foreign key relationship
    def patient_name(self, obj):
        return obj.patient.full_name
    patient_name.short_description = 'Patient Name'


# Register your models here.
admin.site.register(RetinaPhotoModel, RetinaPhotoAdmin)
